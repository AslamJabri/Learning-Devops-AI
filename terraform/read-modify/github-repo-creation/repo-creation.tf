terraform{
    required_providers {
      github = {
        source = "integrations/github"
        version = "~> 6.0"
        }
    }
}

provider github {
    token = ""
}

resource "github_repository" "terraform-repo" {
    name = "new-github-terraform"
    description = "This repo was created by terraform"
    visibility = "public"
  
}