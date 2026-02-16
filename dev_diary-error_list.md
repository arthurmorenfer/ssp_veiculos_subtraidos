Initial Data Analysis & Engineering Decisions

The Context:
The source data is provided in .xlsx format, which is far from optimized for analytical tools. To address this, I initially tested a transformation from the Raw to the Bronze layer using .csv files.

The Challenges:
The transition to CSV immediately introduced several issues:

    Data Integrity: Numerous fields and cells contained nested double quotes (""), requiring significantly more complex data cleaning to maintain the standard CSV structure.

    Storage Inefficiency: The file size ballooned from 63MB (.xlsx) to 127MB (.csv).

The Pivot to Parquet:
Based on these bottlenecks, I decided to move to the .parquet format. The benefits were immediate and substantial:

    Schema Enforcement & Simplified Cleaning: I no longer need to manually handle complex text delimiters for fields that aren't critical for the current analysis.

    Superior Compression: File size dropped from 127MB to a mere 16MB.

    Enhanced Performance: Full file read latency in DuckDB was nearly cut in half, dropping from 1.3s to 707ms.

Conclusion:
With this optimized foundation, I can now proceed with the Exploratory Data Analysis (EDA) with a much faster and more reliable pipeline.

Data Quality Challenges:

    Schema Drift/Inconsistency: Discovered inconsistent sheet_names across the Excel source files, necessitating a metadata-driven ingestion strategy.

    Pseudo-Nulls: Identified string literals (e.g., "NULL") acting as placeholders in the raw data, requiring a transformation step to convert them into true NULL values for analytical accuracy.