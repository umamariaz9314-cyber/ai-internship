\# Clustering and Dimensionality Reduction Summary



\## k-Means Implementation

Implemented k-means from scratch and confirmed it matched sklearn's 

implementation on the same data.



\## Choosing k

Both the elbow method and silhouette score agreed on k=4 for the 

synthetic blob dataset. Silhouette score peaked clearly at k=4, 

confirming well-separated, appropriately-sized clusters.



\## Algorithm Comparison

\- k-Means works well on spherical, well-separated clusters (blobs) 

&#x20; but fails on non-convex shapes (moons, circles).

\- DBSCAN handles arbitrary shapes well via density-based grouping, 

&#x20; succeeding where k-means and agglomerative clustering fail.

\- The right algorithm choice depends heavily on the underlying 

&#x20; cluster geometry.



\## Dimensionality Reduction

\- PCA on the digits dataset showed that \~\[X] components capture 

&#x20; 95% of the variance, a significant reduction from 64 original 

&#x20; dimensions.

\- For visualisation, t-SNE and UMAP both produced much more 

&#x20; visually separated digit clusters than PCA, since they preserve 

&#x20; local structure rather than just global variance.

\- PCA remains appropriate for actual preprocessing before modelling; 

&#x20; t-SNE/UMAP are visualisation-only tools.



\## Anomaly Detection

Isolation Forest successfully flagged \~5% of points as anomalies, 

consistent with the contamination parameter set.

