# Aspects of Poverty Analyzer Project Reflection

## What Tools Helped and Which Did Not?
  On the face of the project, we were probably overly optimistic in our time available and our coding expertise to bring the features of our project into reality. Slack and Github were our primary tools as we worked asynchronously on various parts of the project. Having a Github repository set up and tracking all changes was incredibly helpful for both avoiding duplication of effort, and quality control or “second set of eyes” review. Email alerts from Github included the commits and follow-ups in Slack were summaries of work sessions with intended follow-ups or requests for review. We also coordinated when the progress was complete for the week to orchestrate turn-ins. Slack and Github with backup email alerts is likely as simple as a project could risk without putting the project in peril. We were able to coordinate our efforts effectively with these tools and didn’t try others as we anticipated either scheduling difficulties, or learning curves that would distract from the primary project.

## What Would We Do Differently?
If we were to start over, we would have looked at the last class module first for tips on planning our project. We would have used this outline to lay out specific deadlines so that we could more effectively anticipate how much we were able to accomplish in the timeframe and focus on being more effective on a simpler approach. Additionally, looking at the data and sizes before we began planning would have informed our ability to represent these data sizes effectively for users. Our data sets were very large and generally requires specialty programs to represent it effectively. While python can clean and analyze the data, visualizing it in anything less than a full production GIS or Google Earth program that is optimized for that data type proved a difficult hurdle.

## What Would Our Next Steps Be?
If we were to continue working on this project, we think getting a license for ArcGIS or similar program could cut weeks of development time down for the initial sets and representations on the back end. Using this engine we could generate either flat or vector files that can be more easily represented in a browser. We would also likely seek some kind of hosting provider for the data sizes and availability to end users. This would decrease the technical overhead to users to view and analyze the data as well as increase the amount and types of data we can correlate. These solutions all come with significant costs, but provide the end state we initially aimed for. 

## Does Our Project Meet FAIR4RS?
Our project meets all of FAIR principles by measure of the specifics below. There are some subcomponents that are not applicable, and while some of our metadata may have commit IDs and be indexed, we did not import the metadata for our data and some of the code comments were in the code before the first push, resulting in metadata without commit tags or unique identifiers/indexability: 

##	Findability
####	Globally unique Identifier: 
  Yes, using the Github repository URL is unique
####	Distinct identifiers for components: 
  Yes, the components are separate within the Jupyter notebook.
####	Different versions have different identifiers: 
  N/A
####	Described with rich metadata: 
  Yes/No, the software is, the data is but only from the original source (we did not import the data descriptions)
####	Metadata includes identifiers: 
  No
####	Metadata is searchable: 
  No
##	Accessibility
####	Software is retrievable: 
Yes
####	Protocol is open, free, universally implementable: 
Yes
####	Authentication or authorization procedures: 
N/A
####	Metadata is accessible even when software is not: 
Yes
##	Interoperability
####	Software reads, writes, and exchanges data according to community standards: 
Yes, mapping and survey data typically use .csv, .shp, and .kml files all interoperable with this script.
####	Includes references to other objects: 
Yes, documentation and code explain where to retrieve outside data and how to implement it into the code.
##	Reusability 
####	Described with accurate and relevant attributes: 
Yes, there are many comments, and plentiful documentation.
####	Clear and accessible license: 
Yes, CC0 1.0 Universal 
####	Detailed provenance: 
Yes, the Github Wiki and the README are very detailed.
####	Qualified references to other software: 
N/A
####	Meets community standards: 
Yes, code uses and implements typical mapping and census data formats and standards.
