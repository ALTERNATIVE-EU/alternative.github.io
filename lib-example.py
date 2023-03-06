# Import Library
import alternative_lib
from alternative_lib import alternative_client

# Create Client
alt_client = alternative_client.AlternativeClient()

# Get Datasets from organization
metadata = {
    'organization': 'CST',
}
datasets = alt_client.get_datasets(metadata=metadata)

print('Public datasets from the organization:')
for dataset in datasets:
    print(dataset['title'])

# Download Resource
print('Downloading resource: ' + datasets[0]['resources'][0]['name'] + " ...")

alt_client.download_resource(
    resource_url=datasets[0]['resources'][0]['url'],
    filename=datasets[0]['resources'][0]['name']
)
