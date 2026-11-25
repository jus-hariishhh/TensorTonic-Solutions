-- Returns: segment_name, metric_name.
select segments.segment_name, metrics.metric_name from segments cross join metrics order by segments.segment_name, metrics.metric_name;