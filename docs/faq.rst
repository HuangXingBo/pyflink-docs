================================
Frequently Asked Questions (FAQ)
================================

Installation issues
===================

O1: Scala Dependency
--------------------

PyFlink only provides official installation packages which contain JAR packages for Scala 2.11 before Flink 1.15
, Scala 2.12 in Flink 1.15 and without Scala dependency since Flink 1.16. If you want to use Scala 2.12,
you can download the `binary distribution <https://flink.apache.org/downloads.html>`_ of Scala 2.12,
unzip it and then set the environment variable `FLINK_HOME` to point to the unzipped directory. This
makes it use the JAR packages specified by FLINK_HOME instead of the JAR packages under PyFlink installation
package. You can refer to `PyFlink documentation <https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/python/environment_variables/>`_ for more details.

O2: Java gateway process exited before sending its port number
--------------------------------------------------------------
The exception stack is as following:

.. code-block:: java

    Traceback (most recent call last):
      File "/Users/dianfu/code/src/github/pyflink-faq/testing/test_utils.py", line 122, in setUp
        self.t_env = TableEnvironment.create(EnvironmentSettings.in_streaming_mode())
      File "/Users/dianfu/code/src/github/pyflink-faq/testing/.venv/lib/python3.8/site-packages/apache_flink-1.14.4-py3.8-macosx-10.9-x86_64.egg/pyflink/table/environment_settings.py", line 267, in in_streaming_mode
        get_gateway().jvm.EnvironmentSettings.inStreamingMode())
      File "/Users/dianfu/code/src/github/pyflink-faq/testing/.venv/lib/python3.8/site-packages/apache_flink-1.14.4-py3.8-macosx-10.9-x86_64.egg/pyflink/java_gateway.py", line 62, in get_gateway
        _gateway = launch_gateway()
      File "/Users/dianfu/code/src/github/pyflink-faq/testing/.venv/lib/python3.8/site-packages/apache_flink-1.14.4-py3.8-macosx-10.9-x86_64.egg/pyflink/java_gateway.py", line 112, in launch_gateway
        raise Exception("Java gateway process exited before sending its port number")
    Exception: Java gateway process exited before sending its port number

This issue is usually caused by the reason that PyFlink isn't installed correctly. You can verify whether PyFlink is installed correctly as following:

Execute the following command:

.. code-block:: bash

    python -c "import pyflink;import os;print(os.path.dirname(os.path.abspath(pyflink.__file__)))"

It will print something like the following:

.. code-block:: console

    /Users/duanchen/miniconda3/lib/python3.7/site-packages/pyflink

Execute the following command:

.. code-block:: bash

    ls -lh /Users/duanchen/miniconda3/lib/python3.7/site-packages/pyflink

The structure would be as following:

.. code-block:: console

    total 144
    -rw-r--r--   1 duanchen  staff   1.3K Oct 19 16:01 README.txt
    -rw-r--r--   1 duanchen  staff   1.9K Oct 19 16:01 __init__.py
    drwxr-xr-x  11 duanchen  staff   352B Oct 19 16:03 __pycache__
    drwxr-xr-x  25 duanchen  staff   800B Oct 19 16:03 bin
    drwxr-xr-x  22 duanchen  staff   704B Oct 19 16:03 common
    drwxr-xr-x  13 duanchen  staff   416B Oct 19 16:03 conf
    drwxr-xr-x  20 duanchen  staff   640B Oct 19 16:03 datastream
    drwxr-xr-x   4 duanchen  staff   128B Oct 19 16:03 examples
    -rw-r--r--   1 duanchen  staff   3.2K Oct 19 16:01 find_flink_home.py
    drwxr-xr-x  25 duanchen  staff   800B Oct 19 16:03 fn_execution
    -rw-r--r--   1 duanchen  staff   9.1K Oct 19 16:01 gen_protos.py
    -rw-r--r--   1 duanchen  staff   7.7K Oct 19 16:01 java_gateway.py
    drwxr-xr-x  16 duanchen  staff   512B Oct 19 16:03 lib
    drwxr-xr-x  26 duanchen  staff   832B Oct 19 16:03 licenses
    drwxr-xr-x   4 duanchen  staff   128B Oct 19 16:04 log
    drwxr-xr-x   5 duanchen  staff   160B Oct 19 16:03 metrics
    drwxr-xr-x   4 duanchen  staff   128B Oct 19 16:03 opt
    drwxr-xr-x  11 duanchen  staff   352B Oct 19 16:03 plugins
    -rw-r--r--   1 duanchen  staff   1.3K Oct 19 16:01 pyflink_callback_server.py
    -rw-r--r--   1 duanchen  staff    13K Oct 19 16:01 pyflink_gateway_server.py
    -rw-r--r--   1 duanchen  staff   5.3K Oct 19 16:01 serializers.py
    -rw-r--r--   1 duanchen  staff   7.9K Oct 19 16:01 shell.py
    drwxr-xr-x  31 duanchen  staff   992B Oct 19 16:03 table
    drwxr-xr-x   6 duanchen  staff   192B Oct 19 16:03 util
    -rw-r--r--   1 duanchen  staff   1.1K Oct 19 16:01 version.py

Please check whether the directories `lib`, `opt` are available. Besides, the jar packages under these directories should be as following:

.. code-block:: console

    (base) ➜  pyflink ls -lh /Users/duanchen/miniconda3/lib/python3.7/site-packages/pyflink/lib
    total 401216
    -rw-r--r--  1 duanchen  staff   190K Oct 19 16:02 flink-cep-1.15.2.jar
    -rw-r--r--  1 duanchen  staff   475K Oct 19 16:02 flink-connector-files-1.15.2.jar
    -rw-r--r--  1 duanchen  staff    93K Oct 19 16:02 flink-csv-1.15.2.jar
    -rw-r--r--  1 duanchen  staff   110M Oct 19 16:02 flink-dist-1.15.2.jar
    -rw-r--r--  1 duanchen  staff   171K Oct 19 16:02 flink-json-1.15.2.jar
    -rw-r--r--  1 duanchen  staff    20M Oct 19 16:02 flink-scala_2.12-1.15.2.jar
    -rw-r--r--  1 duanchen  staff    10M Oct 19 16:02 flink-shaded-zookeeper-3.5.9.jar
    -rw-r--r--  1 duanchen  staff    15M Oct 19 16:02 flink-table-api-java-uber-1.15.2.jar
    -rw-r--r--  1 duanchen  staff    35M Oct 19 16:02 flink-table-planner-loader-1.15.2.jar
    -rw-r--r--  1 duanchen  staff   2.9M Oct 19 16:02 flink-table-runtime-1.15.2.jar
    -rw-r--r--  1 duanchen  staff   203K Oct 19 16:02 log4j-1.2-api-2.17.1.jar
    -rw-r--r--  1 duanchen  staff   295K Oct 19 16:02 log4j-api-2.17.1.jar
    -rw-r--r--  1 duanchen  staff   1.7M Oct 19 16:02 log4j-core-2.17.1.jar
    -rw-r--r--  1 duanchen  staff    24K Oct 19 16:02 log4j-slf4j-impl-2.17.1.jar

    (base) ➜  pyflink ls -lh /Users/duanchen/miniconda3/lib/python3.7/site-packages/pyflink/opt
    total 76736
    -rw-r--r--  1 duanchen  staff    37M Oct 19 16:02 flink-python_2.12-1.15.2.jar
    -rw-r--r--  1 duanchen  staff   472K Oct 19 16:02 flink-sql-client-1.15.2.jar

Usage issues
============

O1: How to prepare Python Virtual Environment
---------------------------------------------

You can execute the following script to prepare a Python virtual env zip which can be used on Mac OS and most Linux distributions.

.. code-block:: bash
    :linenos:
    :emphasize-lines: 19

    set -e
    # download miniconda.sh
    if [[ `uname -s` == "Darwin" ]]; then
        wget "https://repo.continuum.io/miniconda/Miniconda3-4.7.10-MacOSX-x86_64.sh" -O "miniconda.sh"
    else
        wget "https://repo.continuum.io/miniconda/Miniconda3-4.7.10-Linux-x86_64.sh" -O "miniconda.sh"
    fi

    # add the execution permission
    chmod +x miniconda.sh

    # create python virtual environment
    ./miniconda.sh -b -p venv

    # activate the conda python virtual environment
    source venv/bin/activate ""

    # specify your apache-flink version and you can add other dependencies
    pip install "apache-flink==$1"

    # deactivate the conda python virtual environment
    conda deactivate

    # remove the cached packages
    rm -rf venv/pkgs

    # package the prepared conda python virtual environment
    zip -r venv.zip venv


O2: How to add Python Files
---------------------------

You can use the command-line arguments `pyfs <https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/deployment/cli/#submitting-pyflink-jobs>`_


.. code-block:: bash

    $ ./bin/flink run --python examples/python/table/word_count.py --pyFiles file:///user.txt,hdfs:///$namenode_address/username.txt

For example, if you have a directory named `myDir` which has the following hierarchy:

.. code-block:: console

    myDir
    ├──utils
        ├──__init__.py
        ├──my_util.py



You can add the Python files of directory `myDir` as following:


.. code-block:: python

    table_env.add_python_file('myDir')

    def my_udf():
        from utils import my_util

JDK issues
==========

O1: InaccessibleObjectException: Unable to make field private final byte[] java.lang.String.value accessible: module java.base does not "opens java.lang" to unnamed module @4e4aea35
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. code-block:: console

    : java.lang.reflect.InaccessibleObjectException: Unable to make field private final byte[] java.lang.String.value accessible: module java.base does not "opens java.lang" to unnamed module @4e4aea35
        at java.base/java.lang.reflect.AccessibleObject.checkCanSetAccessible(AccessibleObject.java:354)
        at java.base/java.lang.reflect.AccessibleObject.checkCanSetAccessible(AccessibleObject.java:297)
        at java.base/java.lang.reflect.Field.checkCanSetAccessible(Field.java:178)
        at java.base/java.lang.reflect.Field.setAccessible(Field.java:172)
        at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:106)
        at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:132)
        at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:132)
        at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:132)
        at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:132)
        at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:69)
        at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.clean(StreamExecutionEnvironment.java:2138)
        at org.apache.flink.table.planner.plan.nodes.exec.common.CommonExecSink.createSinkFunctionTransformation(CommonExecSink.java:331)
        at org.apache.flink.table.planner.plan.nodes.exec.common.CommonExecSink.applySinkProvider(CommonExecSink.java:306)
        at org.apache.flink.table.planner.plan.nodes.exec.common.CommonExecSink.createSinkTransformation(CommonExecSink.java:146)
        at org.apache.flink.table.planner.plan.nodes.exec.stream.StreamExecSink.translateToPlanInternal(StreamExecSink.java:140)
        at org.apache.flink.table.planner.plan.nodes.exec.ExecNodeBase.translateToPlan(ExecNodeBase.java:134)

This is an issue around Java 17. It still doesn't support Java 17 in Flink. You can refer to FLINK-15736 for more details. To solve this issue, you need to use JDK 1.8 or JDK 11.

Connector issues
================

O1: Could not find any factory for identifier 'xxx' that implements 'org.apache.flink.table.factories.DynamicTableFactory' in the classpath
--------------------------------------------------------------------------------------------------------------------------------------------

.. code-block:: console

    Exception Stack:

    py4j.protocol.Py4JJavaError: An error occurred while calling o13.execute.
    : org.apache.flink.table.api.ValidationException: Unable to create a source for reading table 'default_catalog.default_database.sourceKafka'.

    Table options are:

    'connector'='kafka'
    'format'='json'
    'properties.bootstrap.servers'='192.168.101.109:9092'
    'scan.startup.mode'='earliest-offset'
    'topic'='pyflink_test'
        at org.apache.flink.table.factories.FactoryUtil.createTableSource(FactoryUtil.java:150)
        at org.apache.flink.table.planner.plan.schema.CatalogSourceTable.createDynamicTableSource(CatalogSourceTable.java:116)
        at org.apache.flink.table.planner.plan.schema.CatalogSourceTable.toRel(CatalogSourceTable.java:82)
        at org.apache.calcite.rel.core.RelFactories$TableScanFactoryImpl.createScan(RelFactories.java:495)
        at org.apache.calcite.tools.RelBuilder.scan(RelBuilder.java:1099)
        at org.apache.calcite.tools.RelBuilder.scan(RelBuilder.java:1123)
        at org.apache.flink.table.planner.plan.QueryOperationConverter$SingleRelVisitor.visit(QueryOperationConverter.java:351)
        at org.apache.flink.table.planner.plan.QueryOperationConverter$SingleRelVisitor.visit(QueryOperationConverter.java:154)
        at org.apache.flink.table.operations.CatalogQueryOperation.accept(CatalogQueryOperation.java:68)
        at org.apache.flink.table.planner.plan.QueryOperationConverter.defaultMethod(QueryOperationConverter.java:151)
        at org.apache.flink.table.planner.plan.QueryOperationConverter.defaultMethod(QueryOperationConverter.java:133)
        at org.apache.flink.table.operations.utils.QueryOperationDefaultVisitor.visit(QueryOperationDefaultVisitor.java:92)
        at org.apache.flink.table.operations.CatalogQueryOperation.accept(CatalogQueryOperation.java:68)
        at org.apache.flink.table.planner.plan.QueryOperationConverter.lambda$defaultMethod$0(QueryOperationConverter.java:150)
        at java.util.Collections$SingletonList.forEach(Collections.java:4824)
        at org.apache.flink.table.planner.plan.QueryOperationConverter.defaultMethod(QueryOperationConverter.java:150)
        at org.apache.flink.table.planner.plan.QueryOperationConverter.defaultMethod(QueryOperationConverter.java:133)
        at org.apache.flink.table.operations.utils.QueryOperationDefaultVisitor.visit(QueryOperationDefaultVisitor.java:47)
        at org.apache.flink.table.operations.ProjectQueryOperation.accept(ProjectQueryOperation.java:76)
        at org.apache.flink.table.planner.calcite.FlinkRelBuilder.queryOperation(FlinkRelBuilder.scala:184)
        at org.apache.flink.table.planner.delegation.PlannerBase.translateToRel(PlannerBase.scala:219)
        at org.apache.flink.table.planner.delegation.PlannerBase$$anonfun$1.apply(PlannerBase.scala:182)
        at org.apache.flink.table.planner.delegation.PlannerBase$$anonfun$1.apply(PlannerBase.scala:182)
        at scala.collection.TraversableLike$$anonfun$map$1.apply(TraversableLike.scala:234)
        at scala.collection.TraversableLike$$anonfun$map$1.apply(TraversableLike.scala:234)
        at scala.collection.Iterator$class.foreach(Iterator.scala:891)
        at scala.collection.AbstractIterator.foreach(Iterator.scala:1334)
        at scala.collection.IterableLike$class.foreach(IterableLike.scala:72)
        at scala.collection.AbstractIterable.foreach(Iterable.scala:54)
        at scala.collection.TraversableLike$class.map(TraversableLike.scala:234)
        at scala.collection.AbstractTraversable.map(Traversable.scala:104)
        at org.apache.flink.table.planner.delegation.PlannerBase.translate(PlannerBase.scala:182)
        at org.apache.flink.table.api.internal.TableEnvironmentImpl.translate(TableEnvironmentImpl.java:1665)
        at org.apache.flink.table.api.internal.TableEnvironmentImpl.translateAndClearBuffer(TableEnvironmentImpl.java:1657)
        at org.apache.flink.table.api.internal.TableEnvironmentImpl.execute(TableEnvironmentImpl.java:1607)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at org.apache.flink.api.python.shaded.py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:244)
        at org.apache.flink.api.python.shaded.py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:357)
        at org.apache.flink.api.python.shaded.py4j.Gateway.invoke(Gateway.java:282)
        at org.apache.flink.api.python.shaded.py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:132)
        at org.apache.flink.api.python.shaded.py4j.commands.CallCommand.execute(CallCommand.java:79)
        at org.apache.flink.api.python.shaded.py4j.GatewayConnection.run(GatewayConnection.java:238)
        at java.lang.Thread.run(Thread.java:748)
    Caused by: org.apache.flink.table.api.ValidationException: Cannot discover a connector using option: 'connector'='kafka'
        at org.apache.flink.table.factories.FactoryUtil.enrichNoMatchingConnectorError(FactoryUtil.java:587)
        at org.apache.flink.table.factories.FactoryUtil.getDynamicTableFactory(FactoryUtil.java:561)
        at org.apache.flink.table.factories.FactoryUtil.createTableSource(FactoryUtil.java:146)
        ... 45 more
    Caused by: org.apache.flink.table.api.ValidationException: Could not find any factory for identifier 'kafka' that implements 'org.apache.flink.table.factories.DynamicTableFactory' in the classpath.

    Available factory identifiers are:

    blackhole
    datagen
    filesystem
    print
        at org.apache.flink.table.factories.FactoryUtil.discoverFactory(FactoryUtil.java:399)
        at org.apache.flink.table.factories.FactoryUtil.enrichNoMatchingConnectorError(FactoryUtil.java:583)
        ... 47 more


It reuses the Java connectors implementations in PyFlink and most connectors are not bundled in the
official PyFlink (and also Flink) distribution except the following connectors: blackhole, datagen,
filesystem and print. So you need to specify the connector JAR package explicitly when executing PyFlink jobs:

+ The connector JAR package could be found in the corresponding connector page in the official Flink documentation. For example, you can open the `Kafka connector page <https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/kafka/>`_ and search keyword "SQL Client JAR" which is a fat JAR of Kafka connector.

+ It should be noted that you should use the fat JAR which contains all the dependencies. Besides, the version of the connector JAR should be consistent with PyFlink version.

+ For how to specify the connector JAR in PyFlink jobs, you can refer to the `dependency management page <https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/python/dependency_management/#jar-dependencies>`_ of official PyFlink documentation.

O2: ClassNotFoundException: com.mysql.cj.jdbc.Driver
----------------------------------------------------

.. code-block:: java

    py4j.protocol.Py4JJavaError: An error occurred while calling o13.execute.
    : org.apache.flink.runtime.client.JobExecutionException: Job execution failed.
    ...
    Caused by: java.io.IOException: unable to open JDBC writer
        at org.apache.flink.connector.jdbc.internal.JdbcOutputFormat.open(JdbcOutputFormat.java:145)
        at org.apache.flink.connector.jdbc.internal.GenericJdbcSinkFunction.open(GenericJdbcSinkFunction.java:52)
        at org.apache.flink.api.common.functions.util.FunctionUtils.openFunction(FunctionUtils.java:34)
        at org.apache.flink.streaming.api.operators.AbstractUdfStreamOperator.open(AbstractUdfStreamOperator.java:100)
        at org.apache.flink.streaming.api.operators.StreamSink.open(StreamSink.java:46)
        at org.apache.flink.streaming.runtime.tasks.RegularOperatorChain.initializeStateAndOpenOperators(RegularOperatorChain.java:110)
        at org.apache.flink.streaming.runtime.tasks.StreamTask.restoreGates(StreamTask.java:711)
        at org.apache.flink.streaming.runtime.tasks.StreamTaskActionExecutor$1.call(StreamTaskActionExecutor.java:55)
        at org.apache.flink.streaming.runtime.tasks.StreamTask.restoreInternal(StreamTask.java:687)
        at org.apache.flink.streaming.runtime.tasks.StreamTask.restore(StreamTask.java:654)
        at org.apache.flink.runtime.taskmanager.Task.runWithSystemExitMonitoring(Task.java:958)
        at org.apache.flink.runtime.taskmanager.Task.restoreAndInvoke(Task.java:927)
        at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:766)
        at org.apache.flink.runtime.taskmanager.Task.run(Task.java:575)
        at java.lang.Thread.run(Thread.java:748)
    Caused by: java.lang.ClassNotFoundException: com.mysql.cj.jdbc.Driver
        at java.net.URLClassLoader.findClass(URLClassLoader.java:382)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:418)
        at org.apache.flink.util.FlinkUserCodeClassLoader.loadClassWithoutExceptionHandling(FlinkUserCodeClassLoader.java:64)
        at org.apache.flink.util.ChildFirstClassLoader.loadClassWithoutExceptionHandling(ChildFirstClassLoader.java:74)
        at org.apache.flink.util.FlinkUserCodeClassLoader.loadClass(FlinkUserCodeClassLoader.java:48)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:351)
        at org.apache.flink.runtime.execution.librarycache.FlinkUserCodeClassLoaders$SafetyNetWrapperClassLoader.loadClass(FlinkUserCodeClassLoaders.java:172)
        at java.lang.Class.forName0(Native Method)
        at java.lang.Class.forName(Class.java:348)
        at org.apache.flink.connector.jdbc.internal.connection.SimpleJdbcConnectionProvider.loadDriver(SimpleJdbcConnectionProvider.java:90)
        at org.apache.flink.connector.jdbc.internal.connection.SimpleJdbcConnectionProvider.getLoadedDriver(SimpleJdbcConnectionProvider.java:100)
        at org.apache.flink.connector.jdbc.internal.connection.SimpleJdbcConnectionProvider.getOrEstablishConnection(SimpleJdbcConnectionProvider.java:117)
        at org.apache.flink.connector.jdbc.internal.JdbcOutputFormat.open(JdbcOutputFormat.java:143)


This indicates that it the JDBC driver JAR package is missing. It should be noted that the JDBC driver
is also required when using JDBC connector. The JAR packages of the JDBC drivers could be found in the
`JDBC connector page <https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/jdbc/>`_.

O3: NoSuchMethodError: org.apache.flink.table.factories.DynamicTableFactory$Context.getCatalogTable()Lorg/apache/flink/table/catalog/CatalogTable
-------------------------------------------------------------------------------------------------------------------------------------------------

.. code-block:: java

    java.lang.NoSuchMethodError: org.apache.flink.table.factories.DynamicTableFactory$Context.getCatalogTable()Lorg/apache/flink/table/catalog/CatalogTable;
        at org.apache.flink.streaming.connectors.kafka.table.KafkaDynamicTableFactory.createDynamicTableSource(KafkaDynamicTableFactory.java:145)
        at org.apache.flink.table.factories.FactoryUtil.createTableSource(FactoryUtil.java:147)
        ... 39 more

Runtime issues
==============

Q1: OverflowError: timeout value is too large
---------------------------------------------

.. code-block:: console

    File "D:\Anaconda3\envs\py37\lib\threading.py", line 926, in _bootstrap_inner
        self.run()
    File "D:\Anaconda3\envs\py37\lib\site-packages\apache_beam\runners\worker\data_plane.py", line 218, in run
        while not self._finished.wait(next_call - time.time()):
    File "D:\Anaconda3\envs\py37\lib\threading.py", line 552, in wait
        signaled = self._cond.wait(timeout)
    File "D:\Anaconda3\envs\py37\lib\threading.py", line 300, in wait
        gotit = waiter.acquire(True, timeout)
    OverflowError: timeout value is too large

This exception only occurs on Windows. It doesn't affect the execution of PyFlink jobs and so you could
ignore it usually. Besides, you could also upgrade PyFlink versions to 1.12.8, 1.13.7, 1.14.6, 1.15.2 or 1.16.0 where this issue has been fixed.
You could refer to `FLINK-25883 <https://issues.apache.org/jira/browse/FLINK-25883>`_ for more details.

Q2: An error occurred while calling z:org.apache.flink.client.python.PythonEnvUtils.resetCallbackClient
-------------------------------------------------------------------------------------------------------

.. code-block:: console

    py4j.protocol.Py4jError: An error occurred while calling z:org.apache.flink.client.python.PythonEnvUtils.resetCallbackClient. Trace:
    org.apache.flink.api.python.shaded.py4j.Py4jException: Method resetCallbackClient([class java.lang.String, class java.lang.Integer]) does not exist
        at org.apache.flink.api.python.shaded.py4j.reflection.ReflectionEngine.getMethod(ReflectionEngine.java:318)
        ...

This exception only occurs when the version of the flink-python jar (located in site-packages/pyflink/opt)
isn't consistent with PyFlink version. It usually happens when you have tried to install multiple PyFlink
versions and something wrong happens which make multiple versions mixed in your environment. You can
try to reinstall PyFlink in a clean environment.

Data type issues
================

Q1: 'tuple' object has no attribute '_values'
---------------------------------------------

.. code-block:: console

    Caused by: java.util.concurrent.ExecutionException: java.lang.RuntimeException: Error received from SDK harness for instruction 4:
    Traceback (most recent call last):
    File "/usr/local/lib/python3.7/site-packages/apache_beam/runners/worker/sdk_worker.py", line 289, in _execute    response = task()
    File "/usr/local/lib/python3.7/site-packages/apache_beam/runners/worker/sdk_worker.py", line 362, in <lambda>    lambda:
        self.create_worker().do_instruction(request), request)
    File "/usr/local/lib/python3.7/site-packages/apache_beam/runners/worker/sdk_worker.py", line 607, in do_instruction    getattr(request, request_type),
        request.instruction_id)
    File "/usr/local/lib/python3.7/site-packages/apache_beam/runners/worker/sdk_worker.py", line 644, in process_bundle
        bundle_processor.process_bundle(instruction_id))
    File "/usr/local/lib/python3.7/site-packages/apache_beam/runners/worker/bundle_processor.py", line 1000, in process_bundle    element.data)
    File "/usr/local/lib/python3.7/site-packages/apache_beam/runners/worker/bundle_processor.py", line 228, in process_encoded    self.output(decoded_value)  File "apache_beam/runners/worker/operations.py", line 357, in apache_beam.runners.worker.operations.Operation.output
    File "apache_beam/runners/worker/operations.py", line 359, in apache_beam.runners.worker.operations.Operation.output
    File "apache_beam/runners/worker/operations.py", line 221, in apache_beam.runners.worker.operations.SingletonConsumerSet.receive
    File "pyflink/fn_execution/beam/beam_operations_fast.pyx", line 158, in pyflink.fn_execution.beam.beam_operations_fast.FunctionOperation.process
    File "pyflink/fn_execution/beam/beam_operations_fast.pyx", line 174, in pyflink.fn_execution.beam.beam_operations_fast.FunctionOperation.process
    File "pyflink/fn_execution/beam/beam_operations_fast.pyx", line 104, in
        pyflink.fn_execution.beam.beam_operations_fast.IntermediateOutputProcessor.process_outputs
    File "pyflink/fn_execution/beam/beam_operations_fast.pyx", line 158, in pyflink.fn_execution.beam.beam_operations_fast.FunctionOperation.process
    File "pyflink/fn_execution/beam/beam_operations_fast.pyx", line 174, in pyflink.fn_execution.beam.beam_operations_fast.FunctionOperation.process
    File "pyflink/fn_execution/beam/beam_operations_fast.pyx", line 92, in
        pyflink.fn_execution.beam.beam_operations_fast.NetworkOutputProcessor.process_outputs
    File "pyflink/fn_execution/beam/beam_coder_impl_fast.pyx", line 101, in
        pyflink.fn_execution.beam.beam_coder_impl_fast.FlinkLengthPrefixCoderBeamWrapper.encode_to_stream
    File "pyflink/fn_execution/coder_impl_fast.pyx", line 271, in pyflink.fn_execution.coder_impl_fast.IterableCoderImpl.encode_to_stream
    File "pyflink/fn_execution/coder_impl_fast.pyx", line 399, in pyflink.fn_execution.coder_impl_fast.RowCoderImpl.encode_to_stream
    File "pyflink/fn_execution/coder_impl_fast.pyx", line 389, in pyflink.fn_execution.coder_impl_fast.RowCoderImpl.encode_to_streamAttributeError: 'tuple'
        object has no attribute '_values'

This issue is usually caused by the reason that it returns an object other than Row type in a Python
user-defined function, however, the return type of the function is declared as Row. Please double check
the return value of the Python user-defined function to make sure that the type of the returned value
is consitent with the declartion.

Q2: AttributeError: 'int' object has no attribute 'encode'
----------------------------------------------------------

.. code-block:: console

    File "pyflink/fn_execution/beam/beam_operations_fast.pyx", line 71, in pyflink.fn_execution.beam.beam_operations_fast.FunctionOperation.process
    File "pyflink/fn_execution/beam/beam_operations_fast.pyx", line 85, in pyflink.fn_execution.beam.beam_operations_fast.FunctionOperation.process
    File "pyflink/fn_execution/coder_impl_fast.pyx", line 83, in pyflink.fn_execution.coder_impl_fast.TableFunctionRowCoderImpl.encode_to_stream
    File "pyflink/fn_execution/coder_impl_fast.pyx", line 256, in pyflink.fn_execution.coder_impl_fast.FlattenRowCoderImpl._encode_one_row
    File "pyflink/fn_execution/coder_impl_fast.pyx", line 260, in pyflink.fn_execution.coder_impl_fast.FlattenRowCoderImpl._encode_one_row_with_row_kind
    File "pyflink/fn_execution/coder_impl_fast.pyx", line 244, in pyflink.fn_execution.coder_impl_fast.FlattenRowCoderImpl._encode_one_row_to_buffer
    File "pyflink/fn_execution/coder_impl_fast.pyx", line 550, in pyflink.fn_execution.coder_impl_fast.FlattenRowCoderImpl._encode_field_simple
    AttributeError: 'int' object has no attribute 'encode'

This reason to this issue is usually that the actual result value of a Python user-defined function
isn't consistent with the declared result type of the Python user-defined function.

Q3: Types.BIG_INT() VS Types.LONG()
-----------------------------------

It should be noted that Types.BIG_INT() represents type information for the Java BigInteger, while
Types.LONG() represents type information for long integer. There are several users are using Types.BIG_INT()
for long integer by mistake.
