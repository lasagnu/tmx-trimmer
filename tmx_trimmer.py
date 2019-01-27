import xml.etree.ElementTree as ET
import argparse as ARGP

parser = ARGP.ArgumentParser()
parser.add_argument("-s", "--source", type=str,  help="path to source .tmx file", required=True)
parser.add_argument("-p", "--projects", type=str, help="path to file containing project names", required=True)
parser.add_argument("-o", "--output", type=str, help="output file name")
args = parser.parse_args()

project_list = []

if args.source and args.projects:
        try:
                #load and parse source .tmx file
                source_tree = ET.parse(args.source)
                source_root = source_tree.getroot()

                #load and parse file with project names
                projects_tree = ET.parse(args.projects)
                projects_root = projects_tree.getroot()

                #populate project names from the external file
                project_list = [ name.text for name in projects_root.iter('name')]

                #populate unwanted_list with entire tu elements whose project names are not in the project_list
                unwanted_list = [ tu for tu in source_root.iter('tu') if tu[0].text not in project_list ]

                #delete all unwanted projects from root tree
                for all_projects in range(0, len(unwanted_list)):
                        source_root.find('body').remove(unwanted_list[all_projects])

                #save the outcome to separate file
                modified_root = ET.ElementTree(source_root)
                modified_root.write(args.output) if args.output else modified_root.write("output.xml")

        except ET.ParseError as err:

                print(err)

else:
    print(args)
