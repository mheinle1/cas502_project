# Aspects of Poverty Analyzer #

#### Developed by: Zachary Hofstra, Michael Heinle ####
##### [Project Git Repository](https://github.com/mheinle1/cas502_project) #####

## Project Description: ##
The core concept of this project is to develop a way to examine levels and aspects of poverty as experienced by various communities across the United States. While two communities may experience similar levels of poverty, the attributes, or what poverty looks like in each community, may be very different. This project offers a framework for comparing and contrasting the various 'faces' of poverty by focussing on a select catalog of environmental, social, and economic factors that we hope will allow users to go beyond the standard and often used dichotomies of urban vs rural, white vs non-white communities, coastal vs interior geographies, etc.


### Must Have Features:
#### - Graphical Representation of Data on a Map
This feature was successfully implemented.

#### - Representation of Correlation between Overall Poverty Level and Selected Aspects
The original purpose of this function was to allow users to focus on a single aspect of attributes included in the project. As an example, a user could designate a range of overall poverty level, say 20% - 25%, and receive all communities meeting this criteria. The user could then focus the interregation futher by overlaying an additional range associated with a community poverty attribute, say communities where >= 30% of those experiencing poverty also accessed SNAP benefits. While this functionality is central to the usability of the project, its implementation by M.Heinle has not been achieved.

#### - Generation of Comparable Communities based on Selected Aspect Affinity
This function was conceived of as a way to generate outputs of comparable communities based on degree of similar levels of poverty aspect attributes. For instance, each attribute would be given a ranked score for each community based on the proposed weight a given attrubute contributed to a community's overall poverty picture. Users would be able to designate a community or area of interest and receive a mapped output of other communities with shared weighted poverty aspects, such as communities with high home ownership, high unemployment, average educational attainment, and high utilization of SNAP benefits. Performing a comparison these similar communities might allow the user to determine poverty profiles, for instance, the communities described in the example above might represent areas which previously relied on manufacturing. While this functionality is central to the usability of the project, its implementation by M.Heinle has not been achieved.

### Nice to Have Features:
#### - Addition of Interactive Time Series Data
Adding time series data would be relatively straight forward once the intitial ingest and transformation issues have been overcome. Given the generally size of all census files, even single year synopses, time series files would need to be efficiently filtered prior to any further manipulation. 

#### - User Manipulatable Zoom Feature
The simplest implementation of this feature would be to change the GUI and underlying mapping software to GIS specific or GIS capable software such as arcGIS. 

#### - School Zone Overlay
Implementation of this feature would depend on whether or not a GIS specifc GUI was implemented in future iterations. With a GIS specific interface, overlaying school zones would be relatively straight forward. Our team lacks the familiarity with Python based mapping packages to assess how heavy this lift would be in a given package.

## [License](https://github.com/mheinle1/cas502_project/blob/main/LICENSE)
For our team, thoughts about licensing, trademark, and copyright are new issues. We both gravitated toward license structures that committed project code to the public domain and allowed for broadest application and re-use while ensuring that the code could not be claimed or its use and distribution hindered. Our team discussed both CC0 and the Unlicense. After performing a bit of web research, the consensus among the sources we interrogated was that CC0 was more robust and had a more well established legal history at this time. We also preferred the additional liability protection that, at least in appearance, is offered by CC0.


## Documentation
- User Documentation
- [Installation Instructions](https://github.com/mheinle1/cas502_project/blob/main/INSTALL.txt)
- [Testing](https://github.com/mheinle1/cas502_project/tree/main/tests)

#### [Get the latest release of Project Software](https://github.com/mheinle1/cas502_project/releases/tag/v0.1.0)

#### [Cite this Project](https://github.com/mheinle1/cas502_project/blob/main/CITATION.cff)

## Aspects of Poverty Analyzer Project Reflection

### What Tools Helped and Which Did Not?
  On the face of the project, we were probably overly optimistic in our time available and our coding expertise to bring the features of our project into reality. Slack and Github were our primary tools as we worked asynchronously on various parts of the project. Having a Github repository set up and tracking all changes was incredibly helpful for both avoiding duplication of effort, and quality control or “second set of eyes” review. Email alerts from Github included the commits and follow-ups in Slack were summaries of work sessions with intended follow-ups or requests for review. We also coordinated when the progress was complete for the week to orchestrate turn-ins. Slack and Github with backup email alerts is likely as simple as a project could risk without putting the project in peril. We were able to coordinate our efforts effectively with these tools and didn’t try others as we anticipated either scheduling difficulties, or learning curves that would distract from the primary project.

### What Would We Do Differently?
If we were to start over, we would have looked at the last class module first for tips on planning our project. We would have used this outline to lay out specific deadlines so that we could more effectively anticipate how much we were able to accomplish in the timeframe and focus on being more effective on a simpler approach. Additionally, looking at the data and sizes before we began planning would have informed our ability to represent these data sizes effectively for users. Our data sets were very large and generally requires specialty programs to represent it effectively. While python can clean and analyze the data, visualizing it in anything less than a full production GIS or Google Earth program that is optimized for that data type proved a difficult hurdle.

### What Would Our Next Steps Be?
If we were to continue working on this project, we think getting a license for ArcGIS or similar program could cut weeks of development time down for the initial sets and representations on the back end. Using this engine we could generate either flat or vector files that can be more easily represented in a browser. We would also likely seek some kind of hosting provider for the data sizes and availability to end users. This would decrease the technical overhead to users to view and analyze the data as well as increase the amount and types of data we can correlate. These solutions all come with significant costs, but provide the end state we initially aimed for. 

### Does Our Project Meet FAIR4RS?
Our project meets all of FAIR principles by measure of the specifics below. There are some subcomponents that are not applicable, and while some of our metadata may have commit IDs and be indexed, we did not import the metadata for our data and some of the code comments were in the code before the first push, resulting in metadata without commit tags or unique identifiers/indexability: 

####	Findability
#####	Globally unique Identifier: 
  Yes, using the Github repository URL is unique
#####	Distinct identifiers for components: 
  Yes, the components are separate within the Jupyter notebook.
#####	Different versions have different identifiers: 
  N/A
#####	Described with rich metadata: 
  Yes/No, the software is, the data is but only from the original source (we did not import the data descriptions)
#####	Metadata includes identifiers: 
  No
#####	Metadata is searchable: 
  No
####	Accessibility
#####	Software is retrievable: 
Yes
#####	Protocol is open, free, universally implementable: 
Yes
#####	Authentication or authorization procedures: 
N/A
#####	Metadata is accessible even when software is not: 
Yes
####	Interoperability
#####	Software reads, writes, and exchanges data according to community standards: 
Yes, mapping and survey data typically use .csv, .shp, and .kml files all interoperable with this script.
#####	Includes references to other objects: 
Yes, documentation and code explain where to retrieve outside data and how to implement it into the code.
####	Reusability 
#####	Described with accurate and relevant attributes: 
Yes, there are many comments, and plentiful documentation.
#####	Clear and accessible license: 
Yes, CC0 1.0 Universal 
#####	Detailed provenance: 
Yes, the Github Wiki and the README are very detailed.
#####	Qualified references to other software: 
N/A
#####	Meets community standards: 
Yes, code uses and implements typical mapping and census data formats and standards.

