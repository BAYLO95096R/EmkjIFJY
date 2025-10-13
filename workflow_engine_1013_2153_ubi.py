# 代码生成时间: 2025-10-13 21:53:41
# -*- coding: utf-8 -*-

"""
Workflow Engine using Scrapy framework.
This script represents a simple workflow engine that can be used to manage and execute
workflow tasks using Scrapy spiders.
"""

import scrapy


class WorkflowEngine:
    """
    Workflow Engine class that manages the execution of various workflow tasks.
    """
    def __init__(self):
        """Initialize the workflow engine."""
        self.tasks = []

    def add_task(self, task):
        """
        Add a new task to the workflow.

        :param task: A Scrapy Spider class instance.
        """
        if not issubclass(task, scrapy.Spider):
            raise ValueError("Task must be a Scrapy Spider.")
        self.tasks.append(task)

    def run(self):
        """
        Run all the tasks in the workflow.
        """
        for task in self.tasks:
            try:
                # Create an instance of the spider
                spider = task()
                # Set the spider to run in the Scrapy engine
                spider.start_requests()
            except Exception as e:
                # Handle any exceptions that occur during task execution
                print(f"Error running task {task.__name__}: {e}")

# Example usage:
if __name__ == "__main__":
    # Create an instance of the Workflow Engine
    engine = WorkflowEngine()

    # Add some tasks (spiders) to the workflow
    # engine.add_task(MySpider1)
    # engine.add_task(MySpider2)

    # Run the workflow
    engine.run()