#!/usr/bin/env python3

import os
import glob
import argparse


import isce
import isceobj
import shelve 
from isceobj.Util.decorators import use_api
from iscesys import DateTimeUtil as DTU
def createParser():
    '''
    Create command line parser.
    '''

    parser = argparse.ArgumentParser(description='Unzip Alos zip files.')
    parser.add_argument('-i', '--input', dest='input', type=str, required=True,
            help='directory which has all dates as directories. Inside each date, zip files are expected.')
    parser.add_argument('-d', '--dop_file', dest='dopFile', type=str, required=True,
            help='Doppler file for the stack.')
    parser.add_argument('-o', '--output', dest='output', type=str, required=True,
            help='output directory which will be used for unpacking.')
    parser.add_argument('-t', '--text_cmd', dest='text_cmd', type=str, default='source ~/.bash_profile;'
       , help='text command to be added to the beginning of each line of the run files. Example : source ~/.bash_profile;')

    return parser


def cmdLineParse(iargs=None):
    '''
    Command line parser.
    '''

    parser = createParser()
    return parser.parse_args(args = iargs)

def write_xml(shelveFile, slcFile):
    with shelve.open(shelveFile,flag='r') as db:
        frame = db['frame']

    length = frame.numberOfLines 
    width = frame.numberOfSamples

    print (frame) ## To test
    print (width,length)

    slc = isceobj.createSlcImage()
    slc.setWidth(width)
    slc.setLength(length)
    slc.filename = slcFile
    slc.setAccessMode('write')
    slc.renderHdr()
    slc.renderVRT()

  ### Segment edited by TO 2019, to improve import of acquisitions within a day
def get_Date(file):
    import datetime
    #for line in open(file, encoding='ISO-8859-1'):
    for line in file:
        if 'Start Time of Acquisition' in line:
             dt = line[75:-112]
             tStart = datetime.datetime.strptime(dt,"%d-%b-%Y %H:%M:%S %Z")
             filedate = tStart.strftime("%Y%m%dT%H%M")
    print (filedate)
    #file.close()
    return filedate


    #yyyymmddccc='20'+file.split('_')[4]+file.split('_')[3] ### TO modified
    #yyyymmdd=file.split(' ')[0] ### TO modified
    #return yyyymmddccc


    

def main(iargs=None):
    '''
    The main driver.
    '''

    inps = cmdLineParse(iargs)
    
    outputDir = os.path.abspath(inps.output)
    run_unPack = 'run_unPackAlos'

    #######################################
  
    slc_files = glob.glob(os.path.join(inps.input, '*.slc'))
    for file in slc_files:
        annFile = file.replace('_s1_1x1.slc','')+'.ann' ## TO
        imgDate = get_Date(file)
        print (imgDate)
        #annFile = file.replace('*.slc','')+'.ann' ## TO
        print (annFile)
        imgDir = os.path.join(outputDir,imgDate)
        if not os.path.exists(imgDir):
           os.makedirs(imgDir) ### TO
        print (imgDir) ## test TO
        cmd = '/Users/cabrera/Software/isce2/contrib/stack/stripmapStack/unpackFrame_UAVSARTOmodif.py -i ' + annFile  + ' -d '+ inps.dopFile + ' -o ' + imgDir
        print (cmd)
        os.system(cmd)
        
        cmd = 'mv ' + file + ' ' + imgDir
        print(cmd)
        os.system(cmd)

        cmd = 'mv ' + annFile + ' ' + imgDir 
        print(cmd)
        os.system(cmd)

        shelveFile = os.path.join(imgDir, 'data')
        slcFile = os.path.join(imgDir, os.path.basename(file))
        write_xml(shelveFile, slcFile)

if __name__ == '__main__':

    main()


