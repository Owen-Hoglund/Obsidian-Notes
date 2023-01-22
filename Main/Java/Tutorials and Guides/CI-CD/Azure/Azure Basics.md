Many runtime environments:
	.NET, .NET Core, Java, Node.js, Python, Ruby

Resource groups each fall under an Azure subscription, and your Azure account may have multiple subscriptions.

Azure provides infrastructure (IaaS), platform (PaaS), and software (SaaS) each with varying levels of responsibility assigned to either yourself or the cloud provider. 

## Transactional workflows
**ACID**: general data concept

**Atomicity**: each transaction treaded as a single unit, which success completely or fails completely.
	- all-or-none
	- Suppose you define a transaction that contains an Update, Insert, and Delete statement. With atomicity, these statements are treated as a single unit.
**Consistency**: transactions can only take the data in the database from one valid state to another.
	- guarantees that a transaction never leaves your database in a half-finished state.
	-  If one part of transaction fails, all pending changes are rolled back, leaving DB as it was before transaction was initiated.
	-  E.g. When customer record is deleted, you should delete all customer's records from associated tables, i.e. invoices and line items.
	-  properly configured DB wouldn't let you delete the customer record, if that meant leaving its invoices, and other associated records stranded.
**Isolation**: concurrent execution of transactions leave the database in the same state. Transactions separated from each other until they're finished.
	- Configurable in a variety of modes. One mode, transaction blocks until the other transaction finished. Different mode, transaction sees obsolete data from the stae DB was in before previous transaction.
	- Second user may have to wait for first user's deletions to complete before issuing the update. Second user finds that customer has been deleted, which is much better than losing changes without knowing.
**Durability**: Once a transaction has been committed, it will remain committed.
	- Guarantees that the database will keep track of pending changes in such a way that the server can recover from an abnormal termination.
	- Storing uncommitted transactions in a transaction log allows DB server to return to consistent state even if server is unplugged in the middle of a transaction.

**Batch processing**: data elements collected into a group, and whole group is processed at a future time as a batch. Happens on a regular interval basis.

**Stream processing**: each new piece of data processed when it arrives. Constant basis.

Dedicated database instances are faster than elastic pool instances which share from multiple sources. # of users of a web app or more generally the workload or proper memory needed will determine which one is used.

**Azure SQL Managed Instances** allow you to pre-provision compute resources.
- automatic backups, software patching, db monitoring, other admin tasks
- near 100% compatibility with on-premsis SQL server
- supported by other Azure siervices

Azure also supports non-relational (NoSQL) data services. 

**Azure Table** storage key elements are partition key and row key.

**Azure Blob storage**
- [BLOB](https://en.wikipedia.org/wiki/Binary_large_object): binary large object. used in NoSQL dbs, especially key-value store dbs such as [Redis](https://en.wikipedia.org/wiki/Redis).
- block, page, append blobs for different purposes and data sizes.
	- Block: 4.7 TB for large, discrete, binary objects that change infrequently. each block up to 100MB, block blob can contain up to 50000 blocks.
	- Page: up to 8TB, organized as collection of fixed-size 512 byte pages, used to implement vitrual disk storage for VMs. used when random read/write access is required.
	- Append: max size 195GB, used to optimize append operations, 4MB per individual block.

**Azure File Storage**
- file shares in the cloud providing ability to access from anywhere with internet connection
- server message block 3.0 (SMB) to share files
- up to 100TB of data in single storage account
- fully managed - data replicated locally and encrypted at rest.

**Azure Cosmos DB**
- multi-model NoSQL dbms
- manages data as partitioned set of documents
- real time access with fast read/write latencies, >10ms anywhere in world. availability is increased by using multi-region replication.
- takes advantage of Azure scaling and storage capabilities
- premium service, not free.
- ideal for web/retail, gaming, IoT scenarios.

**Provisioning** is running a series of tasks that a service provider performs to create and configure a service.
**Security Principal** is an object that represents a user, group, service, or managed identity that is requesting access to Azure resources.

**Azure Data Factory** is a data integration service that retrieves data from more than one source and converts it continuously and filters it.

**Azure Data Lake** storage is a repo of data organized into directories for omproved file access, supporting POSIX and RBAC permissions, compatible with the Hadoop Distributed File System.

**Azure Databricks** provides big data processing, an Apache Spark-based platform which simplicies provisioning and collaboration of Spark-based analytic solutions utilizing the security capabilities of Azure and allowing integration with Azure data platform services and Power BI.

Other services:
**Azure HDInsight**
**Azure Synapse Analytics**

A **stored procedure** helps us process data as it comes in. In [one example](https://docs.microsoft.com/en-us/learn/modules/create-foundation-modern-apps/8-summary)  `web.AddBusData`, it takes in a new bus route, vehicle, direction, time, and location, and adds it to BusData, then if a bus enters/exits a GeoFence, it will log this info in the GeoFencesActive table.

