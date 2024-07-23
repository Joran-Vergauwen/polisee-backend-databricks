from applicationinsights import TelemetryClient

def create_telemetry_client(instrumentation_key):
    return TelemetryClient(instrumentation_key)

# Function to log custom events to Application Insights
def log_custom_event(tc,event_name, properties=None):
    tc.track_event(event_name, properties=properties)
    tc.flush()

# Function to log custom metrics to Application Insights
def log_custom_metric(tc,metric_name, metric_value):
    tc.track_metric(metric_name, metric_value)
    tc.flush()

# Function to log exceptions to Application Insights
def log_exception(tc,exception):
    tc.track_exception()
    tc.flush()