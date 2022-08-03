Now that we've spent some time with JSON-RPC APIs and Jinja, we're going to change gears and do some work with REST APIs - specifically the CVP REST API.

Before we do anything else, you will need to setup a bearer token for API authentication later in this lab.
Open your ATD CVP instance in a new browser tab if you don't already have it open, and click on the gear icon in the top right of the page.
Under "Access Control" on the lefthand sidebar, click "Service accounts".
Add a new service account, name it anything you want, and give it the role network-admin.
Once you have created this service account, click on the name to bring up a modal.
In this window, under the section titled "Generate Service Account Token" enter a description and a date at least 2 weeks in the future, and then click the blue "Generate" button.
Copy the very long token shown into a file in the lab3 folder of your VSCode instance (see file this.will.not.work.for.you as an example).

After you create your bearer token, on the lefthand sidebar, click "REST API Explorer" near the bottom.
Play around with clicking through this documentation to see what is possible.

1) Using the REST API documentation, determine what endpoints you will need to talk to, to gather the following information
1a) All EOS images currently loaded into CVP
1b) All provisioning containers that currently exist in CVP
2) Print this out nicely, with a Jinja template like so:

Currently, CVP has the following EOS images loaded:
- EOS-4.25.4M.swi
- TerminAttr-1.15.3-1.swix


There are currently 6 provisioning containers in the system:
- Tenant
- Undefined
- Spine
- Hosts
- Leaf
- CVX