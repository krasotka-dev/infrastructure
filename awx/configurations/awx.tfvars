# Below code is used to set backend only
s3_bucket                       =	"anara-ansible-bucket"
s3_folder_region                =	"us-east-1"

# Change to any region to work, in my case default region is us-east-1
region1_vpc_id		    	=	"vpc-d3f5ebb5"

# Change to second region to work, in my case ohio
region2_vpc_id		    	=	"vpc-bd4fb3d6"

# Change to second region to work, in my case n.california
region3_vpc_id		    	=	"vpc-9e766af9"

zone_id			        =	"Z32EBW4NF7YAQH" 
domain			        =	"anarakd.com"
base_domain			=	"anarakd.com"
region1 			= 	"us-east-1"
region2 			= 	"us-east-2"
region3 			= 	"us-west-1"







# Please do not change below
environment                     =   	"tools"
s3_folder_project               =   	"tower"
s3_folder_type                  =   	"tools"
s3_tfstate_file                 =   	"tower.tfstate"
instance_type		        =   	"t2.medium"
user		    	        =	"centos"
key_name			=	"ansible"
ssh_key_location		=	"~/.ssh/id_rsa"
