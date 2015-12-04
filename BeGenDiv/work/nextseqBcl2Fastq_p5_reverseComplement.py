'''
Created on 16.10.2015

@author: maxdriller
'''


    
if __name__ == '__main__':
    
    import argparse

    parser = argparse.ArgumentParser(description="is given a SampleSheet and copies the SampleSheet with the reverse complement of the p5 index")
    parser.add_argument("SampleSheet", help="path and name the SampleSheet", type=str)
    parser.add_argument("out", help="path and name the new SampleSheet", type=str)
    parser.add_argument("--s", "-single", help="enable if single indexed", action="store_true")
    args = parser.parse_args()
    
    sampleS = open(args.SampleSheet)
    
    for line sampleS:
        