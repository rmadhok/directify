""" Supercode to initialize a project directory and keep tidy"""
__author__ = "Raahil"
__copyright__ = "Copyright 2015, The Test Project"
__version__ = "0.0.1"
__maintainer__ = "Raahil"
__email__ = "testemail@gmail.com"


#Import necessary libraries
import os
import datetime
import git

###################################################################
# First thing we need to do is create a parent folder on your 
# machine with the name of your proect. In most cases the parent 
# would be in dropbox. Next, we get the folder path, assign the
# folder name to a variable project_name, and the leading path
# to folder_path
###################################################################
folder_path, project_name = os.path.split(os.getcwd())

# check if running for the first time
first_time = False

# If the folder is empty, except for this python file, the directory is generater
if len(os.listdir(os.getcwd()))==1:
    first_time = True

    # generate folder structure
    os.makedirs(os.getcwd()+'//01_project_management//correspondence')
    os.makedirs(os.getcwd()+'//01_project_management//meetings//agenda')
    os.makedirs(os.getcwd()+'//01_project_management//meetings//minutes')
    os.makedirs(os.getcwd()+'//01_project_management//timeline')
    os.makedirs(os.getcwd()+'//01_project_management//archive')
    os.makedirs(os.getcwd()+'//02_finance//financial_docs//budget')
    os.makedirs(os.getcwd()+'//02_finance//financial_docs//invoices')
    os.makedirs(os.getcwd()+'//02_finance//grants')
    os.makedirs(os.getcwd()+'//02_finance//archive')
    os.makedirs(os.getcwd()+'//03_research_docs//concept_notes')
    os.makedirs(os.getcwd()+'//03_research_docs//documentation')
    os.makedirs(os.getcwd()+'//03_research_docs//literature')
    os.makedirs(os.getcwd()+'//03_research_docs//theory_of_change')
    os.makedirs(os.getcwd()+'//03_research_docs//archive')
    os.makedirs(os.getcwd()+'//04_rct//ab_testing')
    os.makedirs(os.getcwd()+'//04_rct//intervention_material')
    os.makedirs(os.getcwd()+'//04_rct//power_calc')
    os.makedirs(os.getcwd()+'//04_rct//randomization')
    os.makedirs(os.getcwd()+'//04_rct//registry')
    os.makedirs(os.getcwd()+'//04_rct//sampling')
    os.makedirs(os.getcwd()+'//04_rct//archive')
    os.makedirs(os.getcwd()+'//05_survey//archive')
    os.makedirs(os.getcwd()+'//06_data_collection//personnel')
    os.makedirs(os.getcwd()+'//06_data_collection//tracking')
    os.makedirs(os.getcwd()+'//06_data_collection//archive')
    os.makedirs(os.getcwd()+'//07_data_secondary//archive')
    os.makedirs(os.getcwd()+'//08_data_analysis//database')
    os.makedirs(os.getcwd()+'//08_data_analysis//stata')
    os.makedirs(os.getcwd()+'//08_data_analysis//stata//do')
    os.makedirs(os.getcwd()+'//08_data_analysis//stata//data')
    os.makedirs(os.getcwd()+'//08_data_analysis//stata//data//raw')
    os.makedirs(os.getcwd()+'//08_data_analysis//stata//data//clean')
    os.makedirs(os.getcwd()+'//08_data_analysis//stata//log')
    os.makedirs(os.getcwd()+'//08_data_analysis//stata//output//tables')
    os.makedirs(os.getcwd()+'//08_data_analysis//stata//output//plots')
    os.makedirs(os.getcwd()+'//08_data_analysis//stata//qa_qc')
    os.makedirs(os.getcwd()+'//09_outcome//policy_briefs')
    os.makedirs(os.getcwd()+'//09_outcome//press')
    os.makedirs(os.getcwd()+'//09_outcome//reports')
    os.makedirs(os.getcwd()+'//09_outcome//research_papers')
    os.makedirs(os.getcwd()+'//09_outcome//archive')
    os.makedirs(os.getcwd()+'//10_presentations')
    os.makedirs(os.getcwd()+'//11_partners//partner_name//agreements')
    os.makedirs(os.getcwd()+'//11_partners//partner_name//org_structure')


    # generate README.txt file
    file = open("README.txt","w")
    text = 'Project Name: '+project_name+'\nInit Date: '+str(datetime.date.today())
    text = text+'\n'+'Author: '+__author__
    file.write(text)
    file.close()


    #########################################################
    # OPTIONAL: Write a .gitignore file here. You can also 
    # do this directly in a .txt file

    # file = open(".gitignore","w")
    # Write contents of .gitignore file
    # file.write(text)
    # file.close()
    #########################################################

    # initialize a git repo for the project folder
    # repo = git.Repo.init(os.getcwd())
    # assert repo.bare == False
