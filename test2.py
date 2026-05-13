# section B :

# Q1 -->
# append() - it is a method used to add elements to the end of the list. 
# it modifies the original list and does not return a new list. 
# it takes a single argument, which is the element to be added to the list.

list1 = [1,2,3,4]
list1.append(10)
print(list1) # output -> [1, 2, 3, 4, 10]


# Q2 -->
# extend() - it is a method used to add element fromt another list to the end of the list.

list2 = [1,2,3,4]
list3 = [5,6,7,8]
list2.extend(list3)
print(list2)  # ouyput -> [1, 2, 3, 4, 5, 6, 7, 8]

# Q3 -->
# list --- it is mutable , which means we can modified it after creation
# it is ordered which means it maintain the order of the elements as they were added to the list 
# we can have duplicate element in the list 
# we perform slicing and indexing on the list 
# it represent as []
# we can perform add and delete operation on the list 

# tuple --- it is immutable which means we cannot modify it after creation
# it is ordered which means it maintains the order of the elemnts as they were added to the tupple
# we can have duplicate element in the tuple
# we can perform slicing and indexing on the tuple
# it represent as ()
# we cannot perform add and delete operation on the tuple
# we can use tuple to store data that should not be modified, such as coordinates or other fixed values.

# Q4 -->
# pop() - it is a method used to remove and return an elemnt from the list
list4 = [1,2,3,4,5]
print(list4.pop()) # o/p -> 5 it means we use pop() method to remove the last element from the llist it is set by default but we can sepcify the index of the elemnt we want to remove by passing the index as an argument to the opp() method.

print(list4) # o/p -> [1, 2, 3, 4] 

#Q5 -->
# Popperties of sting in python
# 1. Immutable: Strings in Python are immutable, which means that once a string is created, it cannot be modified. Any operation that seems to modify a string actually creates a new string.
# 2. Ordered: Strings maintain the order of characters as they were added to the string
# 3. Indexing and Slicing: You can access individual characters in a string using indexing and slicing, just like you can with lists and tuples.
# 4. Concatenation: You can concatenate strings using the + operator, which creates a new string that is the combinationof the two strings


# SEction C :

# Q1 -->
list5 = [1,2,3,4,5]
list5.append(6)
print(list5) # o/p -> [1, 2, 3, 4, 5, 6]

# Q2 -->
list6 = [1,2,3,4]
list7 = [5,6,7,8]
list6.extend(list7)
print(list6) # o/p -> [1, 2, 3, 4, 5, 6, 7, 8]

# Q3 -->
city ={"raipur","pune","mumbai","hyderabad"}
print(city) # o/p -> {'pune', 'mumbai', 'raipur', 'hyderabad'}  

#Q4 -->
list8 = [1,2,3,4,5]
print(list8.pop()) # o/p -> 5
print(list8) # o/p -> [1, 2, 3, 4]

#Q5 -->
string1 = "hello world"
print(len(string1)) # o/p -> 11

# section D :

#Q1 -->
# Chain of thought

#Q2 -->
# multi agent 

#Q3 -->
# Skeleton of thought

#Q4 -->
#chain of verifiation

#Q5 -->
# no answer

#Q6 -->
# reason + act

#Q7 -->
# Tree of thought

#Q8 -->
# reflexion -its generate initial answer -> self evaluate the answers like critique -> final answer

#Q9 -->
#DSPy based on declarative programming structure for language models like LLM

#Q10 -->
# chain of thoughts, tree of thoughts, ReAct

# section E:

# Q1--> 
""" 
you are an acdemic perfomnace analyst.

your tasks to analyze the performance of students in a class based on their grades and attendance records.

[your csv data for student ]


1. claculate overall class performance
 - calculate the average grade for the class
 - calculate the average attendance for the class

2. identify top performers
    - identify the students with the highest grades
    - identify the students with the highest attendance

3. identify students at risk
    - identify the students with the lowest grades
    - identify the students with the lowest attendance

4. provide insights
    - provide insights into the factors that may be contributing to the performance of the students, such as study habits, extracurricular activities, or other factors that may be impacting their performance.
    - provide insights into the factors that may be contributing to the performance of the class as a whole, such as teaching methods, curriculum, or other factors that may be impacting the performance of the students.

5. provide recommendations
    - provide recommendations for improving the performance of the class as a whole
    - provide recommendations for improving the performance of individual students at risk

    
think step by step before reaching conclusion

output should be presented 
1. summary
2. statistics analysis
3. insights
4. recommendations
5. action plan
6. conclusion
 
"""

#Q2 -->
""""
you are a senoir bussiness strategy analyst using the Reason + Act framework.

you objective is to determine why a bussiness experience low sales and provide actionable recommendations to improve sales.

follow this process repeatedly until you reach a satisfactory conclusion.

thought:
 -analyze sales data to identify trends and patterns
 - conduct market research to understand customer needs and preferences
 - identify missing data
 - and decide on the next steps to take based on the analysis and research

Action:
    request or analyze relevant bussiness data
    such as 
    - sales data
    - customer feedback
    - market research data
    - competitor analysis data
    - financial data
    -seasonal patterns data
    -inventory data
    -website analytics data
    - social media data
    - advertising data
    - pricing data

observation:
    - summarize findings from the data
    - identify patterns, anaomalies or correlations

repeate the cycl until the root causes became clear

ALso - do not jump to conclsion
     - consider multiple possible causes
     - evaluate the potential impact of each cause
     - prioritize the causes based on their impact and likelihood

possible ivestigation ares:
    - product quality issues
    - pricing strategy
    - marketing and advertising effectiveness
    - customer service and support
    - competition and market trends
    - economic factors
    - distribution and supply chain issues
    - seasonal patterns
    - inventory management
    - website and online presence


output should be presented in a structured format, including:
1. summary of findings
2. analysis of potential causes
3. actionable recommendations
4. implementation plan
5. conclusion

"""


#Q3 -->
"""
you are a coutomer retention strategy expert

your objective is to develop a strategy to improve customer retention using the self-cinsistecy prompting method

instructions:

1. independetly generate 5 different solution paths for improving coustomer retentions
2. evaluate each solution path based on its potential impact, feasibility, and alignment with the company's goals and values
3. select the most promising solution path and develop a detailed strategy for implementing it, including specific actions, timelines, and metrics for success
4. implement the strategy and monitor its effectiveness over time, making adjustments as needed based on feedback and results
5. repeat the process periodically to ensure that the customer retention strategy remains effective and aligned with the company's goals and values
6. document the process and outcomes to share with stakeholders and inform future strategy development

important:
- do not jump to conclusion
- consider multiple solution paths
- evaluate the potential impact and feasibility of each solution path
- align the strategy with the company's goals and values

output should be presented in a structured format, including:
solution2:
- strategy
- implementation plan
- metrics for success
- risks
- expected impact

upto solution5 

Final Self-Consistency Analysis
- Common patterns across solutions
- Most reliable strategy
- Highest ROI strategy
- Recommended combined approach
- Final recommendation

"""

#Q4 -->
"""

You are an expert project strategist.

Use Skeleton-of-Thought prompting to create a structured project plan.

Instructions:
1. Define the project objective and scope clearly.
2. Break down the project into key phases and milestones.
3. For each phase, identify the critical tasks and deliverables.
4. Assign responsibilities and resources for each task.
5. Develop a timeline for the project, including deadlines for each phase and task.
6. Identify potential risks and develop mitigation strategies.
7. Establish metrics for success and a plan for monitoring progress.
8. Document the project plan in a clear and organized format to share with stakeholders.

step 1- create project skeleton

generate:
- project objective
- project scope
- key phases
- milestones
- critical tasks
- deliverables
- responsibilities
- resources
- timeline
- potential risks
- mitigation strategies
- metrics for success
- monitoring plan

step 2 - expend each phase
for each phase:
- break down critical tasks into subtasks
- assign specific responsibilities and resources for each subtask
- develop a detailed timeline for each subtask
- identify potential risks for each subtask and develop mitigation strategies
- establish metrics for success for each subtask and a plan for monitoring progress
step 3 - review and refine the project plan
- review the project plan for completeness and clarity
- refine the plan based on feedback from stakeholders and team members
- ensure that the plan is realistic and achievable within the given timeline and resources
- finalize the project plan and share it with all stakeholders

output should be
presented in a structured format, including:
1. project objective and scope
2. key phases and milestones
3. critical tasks and deliverables
4. responsibilities and resources
5. timeline and deadlines
6. potential risks and mitigation strategies
7. metrics for success and monitoring plan



"""


#Q5 --> 
"""
You are a senior marketing strategist using the Reflexion prompting framework.

Your task is to analyze and improve a weak marketing strategy through iterative self-reflection and refinement.

Process:

Phase 1 — Initial Analysis
1. Review the current marketing strategy.
2. Identify:
   - weaknesses
   - missing elements
   - poor assumptions
   - ineffective channels
   - targeting issues
   - messaging problems
   - budget inefficiencies
   - low-conversion areas

3. Generate an initial improved strategy.

Phase 2 — Reflexion (Self-Evaluation)
Critically reflect on the improved strategy.

Ask:
- What parts are still weak?
- What assumptions may be incorrect?
- Which recommendations lack evidence?
- What risks were overlooked?
- Which customer segments are underserved?
- Are there scalability concerns?
- Are there stronger alternatives?

Identify mistakes, gaps, and missed opportunities.

Phase 3 — Strategy Revision
Revise the strategy using insights from the reflection step.

Improve:
- positioning
- customer targeting
- acquisition channels
- retention tactics
- pricing communication
- campaign structure
- content strategy
- performance metrics

Phase 4 — Final Optimization
Perform one final reflection cycle:
- compare original vs revised strategy
- explain why the revised strategy is stronger
- prioritize highest-impact improvements
- recommend execution order

Important Rules:
- Be self-critical
- Avoid defending weak ideas
- Continuously refine reasoning
- Focus on measurable business outcomes
- Use iterative improvement instead of one-shot answers

Output Format:

1. Original Strategy Analysis
2. Identified Weaknesses
3. Initial Improved Strategy
4. Reflexion Analysis
5. Revised Strategy
6. Final Optimization Insights
7. Recommended Action Plan
8. KPIs for Success

Marketing Strategy:
[PASTE CURRENT STRATEGY HERE]
"""

# section F:A company launched a food delivery app but customers are uninstalling the app after first use. Tasks: 1. Identify possible reasons. 2. Suggest solutions. 3. Choose ONE prompting technique suitable for this problem. 4. Write a sample prompt using that technique

"""

1. POssible reasons coustomer are uninstalling the app after first use:
- Poor user experience (slow loading times, difficult navigation)
- Limited restaurant options
- High delivery fees
- Inaccurate delivery times
- Poor customer service
- Lack of promotions or discounts
- Technical issues or bugs in the app

2. Suggested solutions:
- Improve app performance and user interface
- Expand restaurant partnerships to offer more options
- Reduce delivery fees or offer free delivery promotions
- Provide accurate delivery time estimates
- Enhance customer service support
- Implement a loyalty program or offer discounts for repeat customers

3. Suitable prompting technique: Chain of Thought (CoT) prompting

4. Sample prompt using Chain of Thought prompting:

You are a customer retention and business strategy expert.

A food delivery company has launched a new app, but many customers uninstall the app after their first use.

Analyze the problem step-by-step.

Tasks:

1. Identify possible reasons for customer uninstalls.
   Consider:
   - app usability
   - delivery experience
   - pricing
   - customer support
   - technical issues
   - trust and security
   - competition
   - customer expectations

2. For each identified reason:
   - explain why it may cause customers to leave
   - describe its business impact
   - estimate its severity

3. Suggest practical solutions for each problem.
   Include:
   - short-term fixes
   - long-term improvements
   - customer retention strategies

4. Prioritize the solutions based on:
   - impact on retention
   - implementation difficulty
   - cost-effectiveness

5. Create a final action plan for the company.

Important Instructions:
- Think step-by-step before answering.
- Break down the reasoning clearly.
- Avoid jumping directly to conclusions.
- Consider multiple perspectives before deciding the main causes.

Output Format:

1. Problem Analysis
2. Root Causes
3. Step-by-Step Reasoning
4. Recommended Solutions
5. Priority Matrix
6. Final Retention Strategy
7. KPIs to Measure Success

Business Context:
[PASTE BUSINESS DATA HERE]


"""