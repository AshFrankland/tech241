# launch an EC2 instance
# which cloud - aws
# terraform downloads required dependencies
# terraform ini


# provider name
provider "aws"{
	# where in aws
	region = "eu-west-1"	
}
# Launch an ec2 in Ireland
resource "aws_instance" "app_instance"{

# which machine/OS version etc. AMI-id
  ami = var.webapp_ami_id

# what type of instance
  instance_type = "t2.micro"

# is the public IP required
  associate_public_ip_address = true

# what would you like to name it tech241-ash-terraform-app
  tags = {
    Name = "tech241-ash-terraform-app"
  }
}
