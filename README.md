# Logs Analysis
Outputs various reports relating to SQL searches within a newspapers’ database. These reports are printed to the screen and written to an output file named “reports.txt”

## Prerequisites
Access to a operating system capable of installing Vagrant.

## Installing
* Install [VirtualBox 5.1](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* Install [Vagrant](https://www.vagrantup.com/downloads.html)
* In a terminal navigate to the root directory of vagrant.
* Enter the command `vagrant up`, to boot the Vagrant environment
* Enter the command `vagrant ssh`, to login
* Navigate to the folder containing the `logs_analysis.py` file
* Download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) that will be used in the ananlysis
* Unzip the downloaded file and place the `newsdata.sql` file in the working Vagrant directory.
* Enter the command `psql -d news -f newsdata.sql` to connect the database server and execute the necessary SQL commands to create tables and corresponding data.

#### Running the tests
* Enter the command `python logs_analysis.py`, to run the analysis.

#### Built With
Python 2.7

#### Authors
Joey Berger