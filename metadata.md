# Metadata

Each dataset has metadata associated with it. Metadata is structured reference data that helps to sort and identify the information it describes.

## Fields

- Title - this title will be unique across the platform, so make it brief but specific
- URL - automatically filled based on title, but can be edited
- Description - add a longer description of the dataset, including information such as what people need to know when using the data
- Tags - add tags that will help people find the data and link it with other related data
- License - it is important to include a license, so that people know how they can use the data
- Organization - choose which organization, that you're a member of, should own the dataset
- Visibility - a public dataset can be seen by anyone, a private one can only be seen by members of the organization owning the dataset or by collaborators of the dataset, and will not show up in searches by other users
- Source - where the data is from
- Version - version of the data
- Author - name of the person or organization responsible for producing the data
- Author e-mail - an e-mail address for the author, to which queries about the data should be sent
- Maintainer - name of the person or organization responsible for maintaining the data
- Maintainer e-mail - details for a second person responsible for the data

### Advanced Metadata for Experiments

When creating/editing a dataset, you can mark the checkbox to be able to set extra fields, related to experiment data:

- Culture medium
- Number of replicates
- Number of cells/well
- Ratio hiPSC-CMs/HCAECs
- Date of experiment
- Toxin
- Age type
- Dimension
- Category
- Content
- Model

### Custom Fields

If you want the dataset metadata to have more fields, you can add a name/key and value for it.

## Find Data

You should be able to find a dataset by typing the title, or some relevant words from the description/metadata, into the search box on any page, containing datasets. On the left side of the `Datasets` page there are also some filters, such as `Organizations`, `Groups`, `Tags`, `Formats`, `Licenses`. Select any number of options to restrict the search. Under the search box there's also an `Order by` field, to sort datasets in any given way. If you want to look for data owned by a particular organization/group, you can search within that from its homepage.

CKAN uses Apache Solr as its search engine. Note that not the whole functionality is offered through the simplified search interface in CKAN or it can differ. CKAN supports two search modes, both are used from the same search field. If the search terms entered into the search field contain no colon (`:`) CKAN will perform a simple search. If the search expression does contain a colon CKAN will perform an advanced search.

### Simple Search

CKAN defers most of the search to Solr and by default it uses the DisMax Query Parser that was primarily designed to be easy to use and to accept almost any input.

The search words typed by the user in the search box defines the main query constituting the essence of the search. Some characters are treated as mandatory (`+`) and prohibited (`-`) modifiers for terms. Text wrapped in balanced quote characters (`“example text”`) is treated as a phrase. By default, all words or phrases specified by the user are treated as optional unless they are preceded by `+` or `-`. CKAN will search for the complete word and when doing simple search wildcards are not supported. Solr applies some preprocessing and stemming when searching. Stemmers remove morphological affixes from words, leaving only the word stem. This may cause, for example, that searching for `testing` or `tested` will show also results containing the word `test`. If the name of the dataset contains words separated by `-` it will consider each word independently in the search.

**Examples**:

- `census` -> will search for all the datasets containing the word `census` in the query fields
- `census +2019` -> will search for all the datasets contaning the word `census` and filter only those matching `2019` too
- `census -2019` -> will search for all the datasets containing the word `census` and will exclude the results featuring `2019`
- `"european census"` -> will search for all the datasets containing the phrase `european census`
- `Testing` -> will search for all the datasets containing the word `Testing` and also `Test` as it is the stem of `Testing`

### Advanced Search

This will be considered a fielded search and the query syntax of Solr will be used to search. This will allow us to use wildcards (`*`), proximity matching (`~`, looks for terms that are within a specific distance from one another) and general features described in <a href="https://solr.apache.org/guide/6_6/searching.html" target="_blank">Solr docs</a>. The basic syntax is `field:term`. Field names may differ from datasets' attributes, the mapping rules are defined in the <a href="https://github.com/ckan/ckan/blob/master/ckan/config/solr/schema.xml" target="_blank">schema.xml</a> file. You can use `title` to search by the dataset name and `text` to look in a catch-all field. CKAN supports fuzzy searches based on the Levenshtein Distance, or Edit Distance algorithm, to do a fuzzy search use the `~` symbol at the end of a single-word term.

**Examples**:

- `title:european` -> will look for all the datasets containing in their title the word `european`
- `title:europ*` -> will look for all the datasets containing in their title a word that starts with `europ`, like `europe` and `european`
- `title:europe || title:australia` -> will look for datasets containing `europe` or `australia` in their title
- `title: "european census" ~ 4` -> will look for datasets, in which the title contains the words `european` and `census` within a distance of 4 words
- `author:powell~` -> words like `jowell` or `pomell` will also be found
