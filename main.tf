// Configure the Google Cloud provider
provider "google" {
 credentials = "${file("serviceaccount.json")}"
 project     = "brew-wolf"
 region      = "us-east4"
}

// Terraform plugin for creating random ids
resource "random_id" "instance_id" {
    byte_length = 8
}

// Terraform plugin to connect go Google Cloud SQL
resource "google_sql_database_instance" "master" {
    name = "master-instance"
    database_version = "POSTGRES_9_6"
    region = "us-east4"

    settings {
        tier = "db-f1-micro"
    }
}

// Terraform plugin to create google SQL user
resource "google_sql_database_user" "users" {
    name = "me"
    instance = "${google_sql_database_instance.master.name}"
    password "appalpha"
}

// A Google Cloud Engine instances
resource "google_compute_instance" "instance-" {
    machine_type = "f1-micro"
    zone         = "us-east4-b"
    name         = "web-${count.index}"
    count        = 2

    boot_disk {
        initialize_params {
            image = "centos-7-v20190326"
        }
    }

    // Make sure docker is installed on all new instances for later steps
    metadata_startup_script = "sudo yum update -y; sudo yum install -y docker; sudo systemctl enable docker; sudo systemctl start docker; sudo docker run -d -p 80:80 us.gcr.io/brew-wolf/app:master; echo \"Deployed $${image_message}\""

    network_interface {
        network = "default"

        access_config {
            // Include this section to give the VM an external ip address
        }
    }


}

resource "google_compute_instance_group" "brew-resources" {
    name        = "brew-wolf-instances"
    description = "Brew Wolf instance group"
    zone        = "us-east4-b"

    instances = ["${google_compute_instance.instance-.*.self_link}"]
    
    named_port {
        name = "http",
        port = "80",
    }
}

resource "google_compute_firewall" "default" {
  name    = "brew-wolf-firewall"
  network = "default"

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["80", "443", "22"]
  }

  source_tags = ["web"]
}

terraform {
  backend "gcs" {
    bucket = "brew-wolf-states"
    prefix = "prod"
    credentials = "serviceaccount.json"
  }
}