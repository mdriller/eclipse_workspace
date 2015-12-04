#! /usr/bin/env python3

# check_run_consistency
#
# DESCRIPTION:
#  Checks for Illumina runs if all necessary files and folders are present.
# RunInfo.xml is parsed for samples to assert that barcode splitting was performed.
# INPUT:
#  1. path to sequencing run folder
# OUTPUT:
#  console output of completeness or missing files
# EXAMPLE:
#  python check_run_consistency.py ~/spree/raw_data/2014/illumina/140328_2013-06-LM-cenococcum-43-to-48-second-run
import os, glob
# run info location
run_info_xml_loc = "RunInfo.xml"
#containing a list of all txt and xml files in the project dir that should be there (except for RUnInfo.xml)
#root_dir_files = ["RTAComplete.txt", "RTAConfiguration.xml", "RTARead1Complete.txt", "RTARead2Complete.txt", "RTARead3Complete.txt", "RTARead4Complete.txt", "RunCompletionStatus.xml", "RunParameters.xml"]
#root_dir_files - RTARead1Comlete.txt - sometimes Read1-4(4 files)but sometimes only 2 or 3... 
root_dir_files = ["RTAComplete.txt", "RTAConfiguration.xml", "RunCompletionStatus.xml", "RunParameters.xml"]
#containing a list of all InterOp files taht should be present
#interOp_files = ["CorrectedIntMetricsOut.bin", "EmpiricalPhasingMetricsOut.bin", "ErrorMetricsOut.bin", "EventMetricsOut.bin", "ExtractionMetricsOut.bin", "PFGridMetricsOut.bin", "RegistrationMetricsOut.bin", "TileMetricsOut.bin"] 
#interOp files vary between the different runs so hard to define which files should be there...
# list of paths expected to be present
paths_to_check = [\
#  "Data/Intensities/BaseCalls/Alignment"\
]

# function to get the amount of cycles out of the RunInfo.xml (since SampleSheet is no longer available)
def get_run_info(path):
    
    import xml.etree.ElementTree as ET
    
    num_cycles = 0
    
    #print(os.path.join(path, run_info_xml_loc))
    
    xml_info = ET.parse(os.path.join(path, run_info_xml_loc))
    root = xml_info.getroot()
    for read_info in root.iter("Read"):
        num_cycles += int(read_info.attrib["NumCycles"])
        
    #print "#cycles = " + str(num_cycles)
    
    return num_cycles



def check_folders(path):
    missing = []
    
    for p in paths_to_check:
        print(os.path.join(path, p))
        if not os.path.isdir(os.path.join(path, p)):
            missing.append(p)
    
    return missing

def check_cycles(bcl_path, cycles):
    missing = []
    
    # check if cycle folders have same number of files
    print("cycles: %s" % cycles)
    for i in range(cycles):
        for ext in ["",".bci"]:
            c_dir = os.path.join(bcl_path, "%04d.bcl.bgzf%s" % (i+1,ext))
            if not os.path.exists(c_dir):
                missing.append(c_dir)
    
    return missing



def check_files(path, cycles):
    
    missing = []
    
    #check if txt and xml files in the project root directory are present
    for file in root_dir_files:
        filepath = os.path.join(path, file)
        #print filepath
        if not os.path.exists(filepath):
            missing.append(filepath)
    '''
    #check if InterOp files are present
    for file in interOp_files:        
        filepath = os.path.join(path, "InterOp", file)
        #print filepath
        if not os.path.exists(filepath):
            missing.append(filepath)
    '''
           
    # check if basecall and cluster location files are present
    fastq_path = os.path.join(path, 'Data', 'Intensities', 'BaseCalls')
    for lane in range(4):
        bcl_path = os.path.join(fastq_path, 'L00%i'%(lane+1))
        
        #check if cluster location file for each lane is present
        loc_path = os.path.join(path, 'Data', 'Intensities', 'L00%i'%(lane+1), "s_%i.locs"%(lane+1))
        if not os.path.exists(loc_path):
            missing.append(loc_path)
        
        # check base call index file (s_[Lane].bci) and filter file(s_[lane].filter) are present in the bcl directories for each lane
        bci_path = os.path.join(os.path.join(bcl_path, "s_" + str(lane+1) + ".bci"))
        filter_path = os.path.join(os.path.join(bcl_path, "s_" + str(lane+1) + ".filter"))

        # check if basecall files are present for each lane
        if not os.path.exists(bci_path) or not os.path.exists(filter_path):
            missing.append(object)
        missing += check_cycles(bcl_path, cycles)
    
    return missing

class coloredPrinter:
    if os.name == "posix":
        OK = '\033[92m'
        WARN = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
    else:
        OK = ''
        WARN = ''
        FAIL = ''
        ENDC = ''
    
    def passed(self, mes):
        print("".join([self.OK, mes, self.ENDC]))
    
    def failed(self, mes):
        print("".join([self.FAIL, mes, self.ENDC]))
    
    def warning(self, mes):
        print("".join([self.WARN, mes, self.ENDC]))
    
    def info(self, mes):
        print(mes)
          

        
if __name__ == '__main__':
 
    import sys
    
    write = coloredPrinter()
    
    aok=True
    if len(sys.argv) > 1:
        run_path = sys.argv[1]
        write.info("Checking sequencing run at '%s'\n" % run_path)
    else:
        write.failed("Please provide location of run folder as parameter.")
        exit(1)
    write.info("Checking if RunInfo.xml is present...")
    if not os.path.exists(os.path.join(run_path, run_info_xml_loc)):
        write.failed("\tRunInfo.xml is missing. Can not run further checks.")
        exit(1)
    else:
        #get the number of cycles from the RunInfo.xml
        num_cycles = get_run_info(run_path)
        write.passed("\tLooks good!")

    write.info("Checking if necessary directories are present...")
    missing_folders = check_folders(run_path)
    if len(missing_folders) == 0:
        write.passed("\tLooks good!")
    else:
        aok = False
        write.failed("\tSome folders are missing:")
        for p in missing_folders:
            write.failed("\t\t%s" % p)
    
    write.info("\nChecking if necessary files are present...")
    missing_files = check_files(run_path, num_cycles)
    if len(missing_files) == 0:
        write.passed("\tLooks good!")
    else:
        aok = False
        write.failed("\tSome files are missing:")
        for p in missing_files:
            write.failed("\t\t%s" % p)
    
    if aok:
        write.passed("\n\nEverything looks good!")
    else:
        write.failed("\n\nThere are problems with this run. Check above for details.")
    
    
