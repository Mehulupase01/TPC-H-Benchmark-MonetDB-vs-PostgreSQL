# TPC-H Benchmark Comparison: MonetDB vs PostgreSQL

## Description  
This project compares the performance of MonetDB and PostgreSQL using the TPC-H benchmark. The comparison focuses on query execution times across two datasets (SF-1 and SF-3), hardware configurations, and the performance of Python implementations for Q1 and Q6.

## Task / Problem Statement  
The task is to evaluate and compare the performance of MonetDB and PostgreSQL using the TPC-H benchmark and Python implementations for queries Q1 and Q6. The focus is to measure the execution time and performance across different DBMSs and hardware setups.

## Sub-Tasks  
1. **Run TPC-H Benchmark**: Execute the 22 queries of the TPC-H benchmark on MonetDB and PostgreSQL using SF-1 and SF-3 datasets.  
2. **Implement Queries Q1 and Q6**: Implement the queries using Python and compare their performance with MonetDB and PostgreSQL.  
3. **Analyze Performance**: Compare the execution times of the queries across the two DBMSs using SF-1 and SF-3 datasets.  
4. **Evaluate Hardware Impact**: Test the performance on two different hardware configurations to assess how hardware influences database performance.

## Implementation Details  
### 1. **Database Setup**  
   - **MonetDB**: Install MonetDB, set up schema, and load SF-1 and SF-3 datasets.  
   - **PostgreSQL**: Install PostgreSQL, set up schema, and load the datasets. Adjust SQL queries for PostgreSQL compatibility.  
   - **Hardware**: Test performance on two different devices with different hardware specifications.

### 2. **TPC-H Benchmark Queries**  
   - The 22 benchmark queries are executed across both databases. These queries test the DBMS’s ability to handle complex analytical queries.  
   - **Query 1 (Q1)**: Group and aggregate data from the `lineitem` table to evaluate DBMS performance on complex joins and aggregations.  
   - **Query 6 (Q6)**: Calculate revenue from `lineitem` for specific dates and discount ranges, testing filtering and summing performance.

### 3. **Python Implementation**  
   - Implement Q1 and Q6 using Python, utilizing `psycopg2` for PostgreSQL and `pymonetdb` for MonetDB to interface with the databases.  
   - Compare the execution times of the Python implementation with those of the DBMSs.

## Metrics and Results

### **Execution Time per Query**

| Query | Device 1 SF-1 (MonetDB ms) | Device 1 SF-1 (PostgreSQL s) | Device 1 SF-3 (MonetDB ms) | Device 1 SF-3 (PostgreSQL s) |
|-------|----------------------------|------------------------------|----------------------------|------------------------------|
| 1     | 0.6472                     | 12.3855                      | 4.8060                     | 9.736                        |
| 2     | 0.0403                     | 133.4467                     | 0.1005                     | 3.634                        |
| 3     | 0.0913                     | 7.7327                       | 0.7568                     | 4.558                        |
| 4     | 0.0753                     | 2.3550                       | 0.5897                     | 37.791                       |
| 5     | 0.0685                     | 0.9685                       | 1.3207                     | 15.375                       |
| 6     | 0.0290                     | 0.8520                       | 0.1340                     | 3.100                        |
| 7     | 0.0725                     | 1.1165                       | 0.9298                     | 1.927                        |
| 8     | 0.1037                     | 1.1077                       | 1.7040                     | 3.344                        |
| 9     | 0.1233                     | 6.2758                       | 1.0030                     | 14.271                       |
| 10    | 0.0715                     | 7.2970                       | 0.5185                     | 6.137                        |
| 11    | 0.0253                     | 0.5565                       | 0.0442                     | 2.938                        |
| 12    | 0.0697                     | 1.8585                       | 0.3568                     | 2.496                        |
| 13    | 0.1967                     | 1.1213                       | 1.3992                     | 4.434                        |
| 14    | 0.0318                     | 0.7177                       | 0.1112                     | 1.244                        |
| 15    | 0.0478                     | 1.6923                       | 0.2158                     | 5.331                        |
| 16    | 0.1542                     | 1.2090                       | 0.2867                     | 3.562                        |
| 17    | 0.0212                     | 453.6142                     | 0.1468                     | 3631.580                     |
| 18    | 0.1392                     | 11.4977                      | 4.3418                     | 41.185                       |
| 19    | 0.0558                     | 1.3965                       | 0.2812                     | 483.374                      |
| 20    | 0.0550                     | 403.0795                     | 0.2527                     | 3621.088                     |
| 21    | 0.1543                     | 59.8703                      | 2.4197                     | 5.808                        |
| 22    | 0.0570                     | 1.2207                       | 0.2292                     | 3.523                        |

### **Execution Time Comparison (Average)**

| Database  | SF-1 Average Execution Time (ms) | SF-3 Average Execution Time (ms) |
|-----------|----------------------------------|----------------------------------|
| MonetDB   | 1.15                             | 2.68                             |
| PostgreSQL| 2.50                             | 16.75                            |

### **Python vs DBMS Execution Time**

| Query  | Python Execution Time (SF-1) | MonetDB Execution Time (SF-1) | PostgreSQL Execution Time (SF-1) |
|--------|------------------------------|-------------------------------|----------------------------------|
| Q1     | 1.508 s                      | 4.806 ms                      | 9.36 s                          |
| Q6     | 135 ms                       | 0.134 ms                      | 3.10 s                          |

## Conclusion  
MonetDB consistently outperformed PostgreSQL in all tested scenarios, particularly when handling larger datasets (SF-3). MonetDB's columnar storage made it more efficient for read-heavy queries, while PostgreSQL showed more variability across hardware setups. MonetDB is the better choice for data-intensive applications that require consistent performance.

## Future Work  
- **Scale-Up Testing**: Perform testing with higher scale factors (SF-10, SF-30) to evaluate DBMS performance on even larger datasets.  
- **Multi-Client Testing**: Extend the testing to include multi-client scenarios to evaluate concurrent query performance.  
- **Advanced Optimizations**: Investigate potential optimizations for PostgreSQL and MonetDB to improve performance, especially for large-scale queries.

## References  
- **TPC-H Benchmark**: [TPC-H Benchmark Documentation](http://www.tpc.org/tpch/)  
- **MonetDB**: [MonetDB Website](https://www.monetdb.org/)  
- **PostgreSQL**: [PostgreSQL Website](https://www.postgresql.org/)
