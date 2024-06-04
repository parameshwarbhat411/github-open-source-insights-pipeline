SELECT
  d.date_month,
  dr.repo_name,
  COUNT(*) as count_stars,
  LAG(count_stars,1) OVER(PARTITION BY dr.repo_name ORDER BY d.date_month)as last_month_count_stars,
  (count_stars/last_year_count_stars) - 1 as mom_growth,
FROM {{ ref('dim_date') }} AS d
  LEFT JOIN {{ ref('fact_stars') }} AS f
  ON EXTRACT(YEAR FROM f.date) = EXTRACT(YEAR FROM d.date_month)
  AND EXTRACT(MONTH FROM f.date) = EXTRACT(MONTH FROM d.date_month)
  JOIN main.dim_repos dr on f.distinct_repo_id = dr.distinct_repo_id
GROUP BY 1, 2