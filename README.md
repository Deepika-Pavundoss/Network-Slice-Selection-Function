# Introduction

One of the key features of 5G is Network Slice Selection Function (NSSF), which enables the creation of customized network slices tailored to specific use cases.      

The 5G Network Slice Selection Function (NSSF) selects the appropriate network slice for users or services based on preferences, QoS requirements, and available resources, enabling customized services and efficient resource allocation in 5G networks.

# Setup and Run:
 
 1) One can either refer the Usability Document and pull images from  Docker Hub and run them
 2) Or the Repository can be setup on your local and the following commands can be run on the Command prompt terminal.
 
    * Creting the Network to ease communication among images: 
      *     docker network create mynetwork

    * In DB directory: 
      *     docker build -t sqldb .
      *     docker run --name mysql-container -p 3307:3306 --network mynetwork -d sqldb

    * In Host directory: 
      *     docker build -t host . 
    * In Request directory: 
      *     docker build -t request .  
    * In RequestAutomate directory: 
      *     docker build -t requestautomate .  
    * In any of the path, in terminal:
      *     docker run -it --rm -d --name uploader --network mynetwork -p 5000:5000 host

    * Application can be run in 2 ways:
      1.  Manual Input:
       *     docker run -it --rm --name listener --network mynetwork  request
      2. Automation:
       *     docker run -it --rm --name automate --network mynetwork  requestautomate

3) To Visualize N22 interface Network Traffic on Grafana, the following setup has to be done:
    * Grafana datasource:
         * host: localhost:3307
         * Database: nssf
         * User: root
         * Password: password
    * Grafana dashboard query:
         *     select datetime as time, value as val from nssf.Network

