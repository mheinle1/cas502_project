# Aspects of Poverty Analyzer

## Developers
This project was created as part of a team assignment for ASU Spring 2025 course CAS502. Methodology and code are developed by [Zachary Hofstra](link) and [Michael Heinle](link). Please report bugs to the project [GitHub repository](link). Similarly, any additional feature requests may be submitted to the repositoty as well.

## Project Overview
This core concept of this project is to develop a way to examine levels and aspects of poverty as experienced by various communities across the United States. While two communities may experience similar levels of poverty, the attributes, or what poverty looks like in each community, may be very different. This project offers a framework for comparing and contrasting the various 'faces' of poverty by focussing on a select catalog of environmental, social, and economic factors that we hope will allow users to go beyond the standard and often used dichotomies of urban vs rural, white vs non-white, coastal vs interior, etc. 

## Challenges

A technical challenge we foresee is correlating all the data with geographic coordinates. While census 
and ACS (American Community Surveys) data employ the census block/census tract geographic identifiers, their use is 
not as common in medical (preferring ZICTA schema), agricultural, and social data sets, even those originating from 
Federal sources. While specialized tools and software (e.g. ArcGIS) exist specifically to mitigate data 
inconsistencies of this type, their cost is generally prohibitive and their use falls more within the domain of 
professionals, potentially limiting reach and audience. We will instead opt for the creation of crosswalks between 
the various geographic identifiers. This will likely lead to a reduction in the total levels of granularity available
 to end users, but will ensure a broader reach while still providing a viable framework for expansion in the future.

## Communication Plan

Our plan for coordination is regular ad hoc Slack updates as we work asynchronously with 
dedicated Sunday zoom calls to go over anything that may be falling back, ensure we are on azimuth for completion, 
and discuss any other improvements we can make to represent the data as well as possible. Mike will implement and 
share a Git repository for data, code, documentation, and version control. We will hold 1 long initial planning
meeting to line out the steps and divide work evenly.

Branching Implementation: Current plan is not to implement branching initially. Should we encounter an approach 
that makes sense for branching, we will implement at that time. Situations that may require branching considerations
include Zach getting stuck and needing outside assistance/Mike's help, divergent data sets that can and should be worked
independently, or parallel efforts on disparate solutions to determine the most effective.  
