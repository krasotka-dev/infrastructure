# Jenkins Module
### This module is used for creating Jenkins environment
## Prerequisites
1. Terraform 0.11.14

### Steps
* clone Repo
* cd infrastructure/jenkins/
    * ls configurations      


### Region
Choose the region you would like to work with. In my case I chose to work with us-east-1. However this is not required you can choose any region. Change below items according to your own AWS account

* vi configurations/YOUR_REGION/jenkins.tfvars
	* s3_bucket                       =   "acirrustech-iaac"         
	* s3_folder_region                =   "us-east-1"               
	* vpc_id                          =   "vpc-1471ad6e"            
	* zone_id                         =   "Z32OHGRMBVZ9LR"       
	* domain                          =   "acirrustech.com"
	* region                          =   "us-east-1"





### Environment Setup
Once above changes are done save the file and run 
* source setenv.sh configurations/YOUR_REGION/jenkins.tfvars

It will set a proper backend.tf file for us. Next run (by changing region of course):

* terraform apply -var-file configurations/YOUR_REGION/jenkins.tfvars





### Output
The output should be similar to this