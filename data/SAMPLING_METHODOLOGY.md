# Data Sampling Methodology

The data provided in the `/data` folder is a curated subset of the [GitHub Archive (GHA)](https://www.gharchive.org/) dataset, which records the public GitHub timeline. As the complete GHA dataset is approximately 17TB in size, it was necessary to sample the data to make it manageable for this project. However, it's important to note that this sampling approach introduces some caveats compared to working with the real-life GHA data, and our data ingestion process will differ slightly. The sampling process was as follows:

1. Seven representative repositories related to data engineering were selected as a starting point, including popular projects like Plotly. What else would you expect, given our love for data?

2. All events for these seven repositories were extracted from the GHA dataset, up until March 27, 2023. This resulted in a total of 244,066 events.

3. To reduce the size of the dataset, fields that are unnecessary for our analysis, such as repository URLs and user IDs, were removed.

4. The original GHA data is organized into hourly JSON files. To make the data more manageable, the events were aggregated into daily JSON files, resulting in a total of 3,840 files.

By using this curated dataset, we can dive into the data and perform meaningful analyses without the need for extensive data preprocessing or prohibitively large computational resources. However, it's crucial to keep in mind that this sampled dataset may not fully represent the entire GHA dataset, and certain insights or patterns unique to the complete dataset may not be discoverable in this subset.
