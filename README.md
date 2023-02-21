# MicroDecrypter, a Decrypter deployed with AWS

A service that can crack encrpted passwords.

## Overview

* Developed and deployed a password decrypter in AWS, employing API Gateway for sending GET requests with a plain text response time of 5ms, and AWS Lambda for password cracking and hash value querying stored in an S3 Bucket
* Look-up dictionary(data.csv) was stored in S3 bucket
* Swagger documentation for the crack station
* Deployment Architechture
<img width="811" alt="image" src="https://user-images.githubusercontent.com/101235319/220413027-3bc9cf6f-c3a4-4021-99a0-de3dc63ab5a8.png">

## Usage

### Success Response

<img width="714" alt="image" src="https://user-images.githubusercontent.com/101235319/220413117-f58ee7f9-1fe8-4bdd-b95f-9c1e3c1636b9.png">

### Failure Response

<img width="734" alt="image" src="https://user-images.githubusercontent.com/101235319/220413179-0943a34b-2e1b-4d28-b1b3-31bc014d2154.png">
