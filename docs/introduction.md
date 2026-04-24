
## Fundamentals of AWS Cloud Computing

This video explains the basics of AWS cloud computing and how different AWS services are used together to build real-world applications. The video is divided into 6 key parts:

### 1. Static Content Hosting & Delivery

*   **S3 (Simple Storage Service):**
    *   S3 is the storage location for all website files, including images, HTML, JavaScript, and CSS.
    *   It is highly reliable and can handle files of any size.
    *   S3 organizes files into buckets, which act as root folders for websites.
*   **CloudFront:**
    *   CloudFront is AWS's Content Delivery Network (CDN).
    *   It copies website files to data centers globally (Edge locations) for fast user access, regardless of location.
    *   CloudFront enhances security with features like signed URLs and cookies for content access control.
    *   It integrates with AWS WAF (Web Application Firewall) to protect websites from cyber attacks.
*   **Route 53:**
    *   Route 53 is AWS's DNS service.
    *   It translates website domain names into IP addresses.
    *   It directs users to the nearest or fastest server location.
    *   It can split traffic for testing new website versions.

### 2. Backend Services / Compute Layer

*   **Serverless with API Gateway & Lambda:**
    *   API Gateway receives requests and routes them to appropriate Lambda functions.
    *   Lambda functions execute code in response to triggers.
    *   Lambda is serverless, meaning AWS manages the underlying servers.
    *   Serverless is ideal for unpredictable workloads and specific tasks.
    *   It scales automatically and charges only for compute time used.
*   **EC2 (Elastic Cloud Compute):**
    *   EC2 provides virtual servers in AWS data centers.
    *   It offers complete control over the server environment, including OS, software, and security.
    *   EC2 is scalable, allowing users to adjust server capacity as needed.
    *   It suits applications needing specific configurations or legacy software.
*   **Containers with ECS (Elastic Container Service):**
    *   ECS manages containers, which package applications and their dependencies.
    *   Containers ensure consistent performance across different environments.
    *   ECS is ideal for microservices architectures.
    *   It allows independent scaling and updates of application components.
    *   It balances serverless and EC2, offering more control than Lambda but less management than EC2.
*   **Elastic Kubernetes Service (EKS):**
    *   Managed service for running Kubernetes on AWS without needing to install and operate your own Kubernetes control plane.
*   **AWS Fargate:**
    *   Serverless compute engine for containers, allowing users to run containers without managing servers.
*   **Lightsail:**
    *   Easiest way to get started with AWS for small-scale applications, offering virtual servers, storage, and networking.
*   **Batch:**
    *   Fully managed service for running batch computing workloads of any scale.

### 3. Data Storage & Management

*   **S3 (Object Storage):**
    *   S3 is object storage, suitable for files like images, videos, and documents.
    *   Files are stored as complete objects and accessed via URLs.
    *   It is best for infrequently modified, complete files.
*   **RDS (Relational Database Service):**
    *   RDS is for traditional SQL databases.
    *   It automatically manages tasks like backups, security, and scaling.
    *   It is suitable for structured data with clear relationships.
    *   Example: e-commerce applications managing orders, customers, and products.
*   **DynamoDB (NoSQL Database):**
    *   DynamoDB is a NoSQL database designed for speed and scalability.
    *   It handles large data volumes with millisecond responses.
    *   It is flexible and best for data that doesn't fit into tables or needs fast access.
    *   Example: tracking delivery driver locations.
*   **EBS (Elastic Block Store):**
    *   Provides persistent block storage volumes for use with Amazon EC2 instances.
*   **EFS (Elastic File System):**
    *   Provides scalable file storage for use with Amazon EC2.
*   **Glacier:**
    *   Secure, durable, and extremely low-cost cloud storage service for data archiving and long-term backup.

### 4. AI and Machine Learning

*   **Amazon Bedrock:**
    *   Bedrock offers pre-built AI models.
    *   It allows easy integration of advanced AI capabilities without building models from scratch.
    *   Useful for quickly adding chatbots or other AI features.
    *   Offers customization and security.
*   **Amazon SageMaker:**
    *   SageMaker is a comprehensive platform for building, training, and deploying custom machine learning models.
    *   It is ideal for complex tasks like predicting user behavior or fraud detection.
    *   Offers full control over AI development.

### 5. Security

*   **VPC (Virtual Private Cloud):**
    *   VPC is a private network within AWS.
    *   It allows control over network configurations, subnets, and internet access.
    *   It uses public subnets for internet-facing resources.
    *   It uses private subnets for internal resources.
    *   NAT Gateways provide secure internet access from private subnets.
*   **IAM (Identity and Access Management):**
    *   IAM controls access to AWS resources.
    *   It ensures users and services have only necessary permissions.
    *   It enables granular permission settings for services like Lambda and EC2.
    *   Crucial for securing AI and machine learning workloads.
*   **Security Tools:**
    *   AWS provides additional security services.
    *   GuardDuty for threat detection.
    *   KMS for encryption key management.
    *   AWS Shield and WAF for cyber attack protection.
*   **Secrets Manager:**
    *   Protects access to applications, services, and IT resources without the upfront investment and on-going maintenance costs of operating your own infrastructure.
*   **AWS CDK (Cloud Development Kit):**
    *   Open-source software development framework to define your cloud application resources using familiar programming languages.
*   **Config:**
    *   Provides AWS resource inventory, configuration history, and configuration change notifications to enable security and governance.

### 6. Monitoring and Auditing

*   **CloudWatch:**
    *   CloudWatch monitors AWS services and applications.
    *   It collects performance metrics, logs, and events.
    *   It provides dashboards and alerts for real-time insights into application performance.
    *   It can automate responses to issues.
*   **CloudTrail:**
    *   CloudTrail records API calls within the AWS account.
    *   It logs all changes made to the AWS environment.
    *   Essential for auditing and security.
    *   Tracks who made changes, when, and what was changed.
    *   Especially important in AI and machine learning for tracking model performance and access.
*   **X-Ray:**
    *   Helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture.

### Networking Services

Networking services facilitate communication between resources and manage traffic.

*   **VPC (Virtual Private Cloud):**
    *   A VPC is a virtual private cloud that isolates your resources from other resources in the AWS cloud. It allows you to launch AWS resources into a virtual network that you've defined.
*   **Subnets:**
    *   A subnet is a range of IP addresses within a VPC. You can create public and private subnets. Public subnets have access to the internet, while private subnets do not.
*   **Security Group:**
    *   A security group acts as a virtual firewall that controls the traffic to and from your EC2 instances. You can specify rules to allow or deny traffic based on IP addresses, protocols, and ports.
*   **Internet Gateway:**
    *   An internet gateway connects your VPC to the internet. It allows communication between instances in your VPC and the internet.
*   **Route Table:**
    *   A route table determines how traffic flows within a VPC. You can create custom route tables for your subnets to control the routing of traffic.
*   **NAT Gateway:**
    *   A NAT Gateway in AWS is a managed Network Address Translation service that allows instances in private subnets to access the internet while preventing external services from initiating connections to those instances.
*   **NACL (Network ACL):**
    *   A Network ACL is a virtual firewall that controls traffic to and from your subnets. It provides an additional layer of security at the subnet level.
*   **Load Balancer:**
    *   A load balancer distributes incoming application traffic across multiple targets, such as EC2 instances, to ensure high availability and reliability.
*   **Direct Connect:**
    *   Direct Connect provides a dedicated network connection from your premises to AWS. It allows you to establish a private connection between AWS and your data center, office, or colocation environment.
*   **Transit Gateway:**
    *   Transit Gateway enables customers to connect their VPCs and their on-premises networks to a single gateway. It simplifies network architecture and reduces the complexity of managing multiple connections.

### Messaging Services

These services enable communication between distributed systems or components.

*   **SQS (Simple Queue Service):**
    *   SQS is a fully managed message queuing service that enables decoupling of microservices, distributed systems, and serverless applications. It allows you to send, store, and receive messages between software components.
*   **SNS (Simple Notification Service):**
    *   SNS is a managed messaging service for sending notifications from the cloud to subscribers or other applications. It supports multiple messaging protocols, including HTTP/HTTPS, email, SMS, and AWS Lambda.
*   **MQ:**
    *   MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that makes it easy to set up and operate message brokers in the cloud. It enables communication between distributed applications and microservices.

---

## The Most Important AWS Services To Know

### Permission and Identity Management

1.  **IAM** — Controls access to AWS resources with granular permissions for users, groups, and roles.
2.  **Identity Center** — Centralized access management for multiple AWS accounts and business applications using SSO.

### Cloud Network Management

1.  **VPC** — Isolated virtual network to launch AWS resources with full control over IP ranges, subnets, and gateways.
2.  **VPN** — Encrypted tunnel connecting on-premises networks to AWS over the public internet.
3.  **Private Link** — Private connectivity between VPCs and AWS services without exposing traffic to the public internet.
4.  **Direct Connect** — Dedicated physical network connection from your data center to AWS for consistent, low-latency throughput.

### DNS

1.  **Route 53** — Highly available DNS service with domain registration, routing policies, and health checks.

### Static Content Hosting & Delivery

1.  **CloudFront** — Global CDN that caches and delivers content from edge locations for low-latency access.
2.  **S3** — Object storage for hosting static websites, images, videos, and any file type at scale.

### APIs

1.  **Load Balancer** — Distributes incoming traffic across multiple targets (EC2, containers, Lambda) for high availability.
2.  **API Gateway** — Fully managed service to create, publish, and secure REST, HTTP, and WebSocket APIs at any scale.

### Security

1.  **WAF** — Web Application Firewall that filters malicious web traffic based on customizable rules.
2.  **Shield** — Managed DDoS protection for applications running on AWS (Standard and Advanced tiers).
3.  **Certificate Manager** — Provisions, manages, and deploys SSL/TLS certificates for AWS services and internal resources.

### User Management

1.  **Amazon Cognito** — User sign-up, sign-in, and access control for web and mobile apps with support for social and enterprise identity providers.

### Compute

1.  **EC2** — Virtual servers with full control over OS, networking, and storage configurations.
2.  **Lightsail** — Simplified compute for small-scale applications with bundled virtual servers, storage, and networking.
3.  **ECS** — Container orchestration service for running and managing Docker containers.
4.  **Fargate** — Serverless compute engine for containers — no server management required.
5.  **EKS** — Managed Kubernetes service for running containerized applications at scale.
6.  **Lambda** — Serverless functions that execute code in response to events, charging only for compute time used.

### Storage

1.  **S3** — Scalable object storage for any data type with lifecycle policies and storage classes.
2.  **EBS** — Persistent block storage volumes attached to EC2 instances.
3.  **EFS** — Scalable, shared file storage accessible from multiple EC2 instances simultaneously.

### Config & Secrets

1.  **Secrets Manager** — Securely stores and rotates database credentials, API keys, and other secrets.
2.  **App Config** — Manages, deploys, and validates application configuration data at runtime.
3.  **KMS** — Creates and manages encryption keys used to encrypt data across AWS services.

### Database

1.  **RDS** — Managed relational databases supporting MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server.
2.  **Aurora** — High-performance, MySQL/PostgreSQL-compatible relational database with up to 5x throughput.
3.  **DynamoDB** — Fully managed NoSQL key-value and document database with single-digit millisecond latency.
4.  **DocumentDB** — Managed MongoDB-compatible document database for JSON workloads.
5.  **Keyspaces** — Managed Apache Cassandra-compatible wide-column database.
6.  **Neptune** — Graph database for building applications that work with highly connected datasets.
7.  **OpenSearch** — Managed search and analytics engine (Elasticsearch-compatible) for log analytics and full-text search.
8.  **DMS** — Database Migration Service for migrating databases to AWS with minimal downtime.

### Caching

1.  **ElastiCache** — Managed in-memory caching with Redis or Memcached for sub-millisecond data access.
2.  **MemoryDB** — Redis-compatible, durable in-memory database for ultra-fast performance with data persistence.

### Application Coordination

1.  **SNS** — Pub/sub messaging service for sending notifications to subscribers via HTTP, email, SMS, or Lambda.
2.  **SQS** — Fully managed message queue for decoupling and scaling microservices and distributed systems.
3.  **EventBridge** — Serverless event bus for routing events between AWS services, SaaS apps, and custom applications.
4.  **Step Functions** — Visual workflow service for orchestrating multi-step serverless applications and microservices.
5.  **MWAA** — Managed Apache Airflow for authoring, scheduling, and monitoring data pipelines and workflows.

### Monitoring & Logging

1.  **CloudWatch** — Collects metrics, logs, and events; provides dashboards and alarms for real-time observability.
2.  **CloudTrail** — Records all API calls and account activity for governance, compliance, and auditing.
3.  **Config** — Tracks AWS resource configurations and evaluates them against desired compliance rules.
4.  **X-Ray** — Traces and debugs distributed applications to identify performance bottlenecks and errors.

### CI/CD

1.  **CodeBuild** — Fully managed build service that compiles source code, runs tests, and produces deployable artifacts.
2.  **CodeDeploy** — Automates application deployments to EC2, Fargate, Lambda, and on-premises servers.
3.  **CodePipeline** — Continuous delivery service that automates release pipelines for fast and reliable updates.

### Infrastructure as Code

1.  **CloudFormation** — Provisions and manages AWS resources using declarative JSON or YAML templates.
2.  **CDK** — Define cloud infrastructure using familiar programming languages (TypeScript, Python, Java, etc.).

### Developer Productivity

1.  **Amplify** — Full-stack development platform for building and deploying web and mobile apps with backend services.
2.  **AppSync** — Managed GraphQL and Pub/Sub API service with real-time data sync and offline capabilities.
3.  **WorkSpaces** — Managed virtual desktop infrastructure (VDI) accessible from any device.
4.  **Amazon Q** — AI-powered assistant for building, operating, and transforming on AWS.
5.  **Amazon MCP** — Model Context Protocol support for connecting AI agents to AWS tools and services.

### Data Processing & Analytics

1.  **S3** — Central data lake storage for raw and processed data at any scale.
2.  **EMR** — Managed big data platform for processing vast amounts of data using Apache Spark, Hadoop, and more.
3.  **Athena** — Serverless interactive query service for analyzing data directly in S3 using SQL.
4.  **Glue** — Serverless ETL service for discovering, preparing, and combining data for analytics and ML.
5.  **Redshift** — Fully managed data warehouse for running complex analytical queries on petabytes of data.
6.  **QuickSight** — Serverless BI service for creating interactive dashboards and visualizations.
7.  **Kinesis** — Real-time data streaming and ingestion service for collecting, processing, and analyzing streaming data.

### AI & Machine Learning

1.  **Bedrock** — Access and customize pre-built foundation models (Claude, Llama, Titan) via a single API.
2.  **SageMaker** — End-to-end platform for building, training, and deploying custom machine learning models.
3.  **Rekognition** — Image and video analysis service for detecting objects, faces, text, and scenes.
4.  **Polly** — Text-to-speech service that converts text into lifelike speech in multiple languages.
5.  **Transcribe** — Automatic speech recognition service that converts audio to text.

---

## AWS+Terraform projects for learning

### Project 1: Static Website Hosting
- **Description**: Deploy a static website using CloudFront as the CDN and S3 as the origin for hosting assets.
- **Services**: CloudFront, S3, Route 53, Certificate Manager, WAF

### Project 2: Serverless REST API
- **Description**: Build a serverless API with user management and token validation, backed by S3 and DynamoDB for storage.
- **Services**: API Gateway, Lambda, S3, DynamoDB, Cognito

### Project 3: Multi-AZ VPC with Immutable Infrastructure
- **Description**: Set up a VPC with multi-AZ public and private subnets, using HashiCorp Packer to bake the application into an Amazon AMI for immutable infrastructure deployments with RDS as the database.
- **Services**: VPC, EC2, RDS, Packer (AMI), ALB, Auto Scaling

### Project 4: Video Uploader & Transcoder
- **Description**: Build a video upload and transcoding pipeline similar to YouTube, where uploads to S3 trigger Lambda functions for processing and transcoding.
- **Services**: S3, Lambda, MediaConvert, CloudFront, DynamoDB, SNS

### Project 5: Event-Driven Data Processing Pipeline
- **Description**: Upload CSV files to S3, buffer them through SQS, and process them with Lambda for transformation and storage.
- **Services**: S3, SQS, Lambda, DynamoDB, CloudWatch

### Project 6: Automatic Security Remediation Bot
- **Description**: Detect insecure changes via CloudTrail logs, trigger an EventBridge rule to invoke a Lambda function that deletes the bad rule, then notify the security team via Slack and SMS using SNS.
- **Services**: CloudTrail, EventBridge, Lambda, SNS, IAM

### Project 7: Silent Scalper
- **Description**: Build a serverless application that monitors stock prices and sends notifications when certain conditions are met.
- **Services**: S3, Lambda, DynamoDB, API Gateway, SNS, CloudWatch

### Project 8: The Smart Vault
- **Description**: Create a secure storage solution for sensitive data with automated backup and monitoring.
- **Services**: EC2, EBS, EventBridge, Lambda, SNS, CloudWatch

### Project 9: AI Customer Service Bot
- **Description**: Develop an AI-powered chatbot for customer service that can handle common queries and escalate complex issues.
- **Services**: S3, Lambda, SNS, Amazon Lex, Amazon Polly

### Project 10: Intelligent Document Engine
- **Description**: Build a document processing system that extracts information from documents and stores it in a searchable database.
- **Services**: S3, Textract, SageMaker, OpenSearch, DynamoDB




