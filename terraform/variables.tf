/* 
variable "project_id" {
  description = "The ID of the project in which to create the bucket."
  type        = string
}
*/

variable "project_id" {
    description = "The ID of the project in which to create the bucket"
    type= string
}

variable "bucket_name" {
    description = "the name of the bucket"
    type = string
    

}


variable "location" {
    description = "The GCS location"
    type = string
   
}

variable "region" {
    description = "Provider region"
    type = string
    
}

variable "storage_class" {
    description = "storage class of the bucket"
    type = string
    default = "STANDARD"
}

variable "force_destroy" {
    description = "When deleting a bucket, this boolean option will delete all contained objects."
    type = bool
    default = false
  
}

variable "enable_versioning" {
    description = "Enable versioning on the bucket"
    type = bool
    default = true
}



