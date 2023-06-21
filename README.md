# Snowflake-2-MongoDB
Sample Kafka Configuration to move data from Snowflake to MongoDB 

#Moving Data from Snowflake to MongoDB using Kafka Connect

Set up a Kafka Connect cluster:https://docs.snowflake.com/en/user-guide/kafka-connector-install

Install and configure Apache Kafka and Kafka Connect.
Ensure that the necessary Kafka Connect connectors are available, such as the Snowflake Connector and MongoDB Connector.
Configure the Snowflake Source Connector:

Define a Snowflake source connector configuration file, let's call it snowflake-source-config.properties, with the necessary properties for connecting to Snowflake and extracting data.
Configure the source connector with the Snowflake JDBC driver, Snowflake connection details, SQL query or table name for data extraction, and other relevant settings.
Example configuration properties for the Snowflake source connector:
```
name=snowflake-source-connector
connector.class=snowflake.kafka.connector.SnowflakeSourceConnector
tasks.max=1
snowflake.topic.prefix=snowflake_data
snowflake.url=jdbc:snowflake://<snowflake-host>:<snowflake-port>/<snowflake-db>?warehouse=<warehouse>&db=<db>&schema=<schema>
snowflake.user=<username>
snowflake.private.key.path=/path/to/private/key.pem
snowflake.private.key.passphrase=<private-key-passphrase>
query=<snowflake-sql-query>
# Alternatively, use table names for data extraction
mode=timestamp
timestamp.column.name=<timestamp-column-name>
```
Adjust the properties according to your Snowflake configuration, including the Snowflake URL, credentials, SQL query, or table names for data extraction.
Configure the MongoDB Sink Connector:

Define a MongoDB sink connector configuration file, let's call it mongodb-sink-config.properties, with the necessary properties for connecting to MongoDB and writing data.
Configure the sink connector with the MongoDB connection details, including the connection URL, authentication credentials, target collection, and any required transformation settings.
Example configuration properties for the MongoDB sink connector:
```
name=mongodb-sink-connector
connector.class=org.apache.kafka.connect.mongodb.MongoDbSinkConnector
tasks.max=1
topics=snowflake_data
connection.uri=mongodb://<username>:<password>@<mongodb-host>:<mongodb-port>/<database>
key.converter=org.apache.kafka.connect.storage.StringConverter
value.converter=org.apache.kafka.connect.json.JsonConverter
value.converter.schemas.enable=false
mongodb.collection=<target-collection>
```
Adjust the properties according to your MongoDB configuration, including the MongoDB connection URL, authentication credentials, target collection, and any other required settings.
Start Kafka Connect:

Start Kafka Connect using the Kafka Connect worker configuration file.

Provide the Snowflake source connector configuration file and the MongoDB sink connector configuration file as command-line arguments:
```
$ kafka-connect-start <kafka-connect-config.properties> snowflake-source-config.properties mongodb-sink-config.properties
```
With this setup, the Snowflake source connector will read data from Snowflake based on the specified SQL query or table names and produce the data as Kafka messages to the snowflake_data topic. The MongoDB sink connector will consume these messages from the topic and write the data to the specified MongoDB collection.

Ensure that you have the necessary Snowflake and MongoDB dependencies available in your Kafka Connect classpath. Refer to the specific documentation of the Snowflake Connector and MongoDB Connector for detailed configuration options and setup instructions.
```
Please double-check all the placeholders, such as <snowflake-host>, <snowflake-port>, <snowflake-db>, <warehouse>, <db>, <schema>, `<username>
```
