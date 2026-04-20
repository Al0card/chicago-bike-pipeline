provider "google" {
    project = var.project_id
    region = var.region
}

resource "google_storage_bucket" "bike_data_lake"{
    name = var.bucket_name
    location = var.location
    storage_class = var.storage_class

    force_destroy = var.force_destroy

    versioning {
        enabled = var.enable_versioning
    }

    uniform_bucket_level_access = true

    
}