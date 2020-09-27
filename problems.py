"""
    Copyright (c) 2015-2020 Raj Patel(raj454raj@gmail.com), StopStalk

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""

from gluon import current
import stopstalk_constants
import utilities

def generate_recommendations(user_id):
    """
    Generate recommendations based on past solved problems.

    @param user_id (Integer): User ID for which recommendations should be generated.
    @return (List): Problem IDs of the new recommendations.
    """
    db = current.db
    ptable = db.problem

    solved_problems, unsolved_problems = utilities.get_solved_problems(user_id, False)

    query = (~ptable.id.belongs(solved_problems)) & \
            (~ptable.id.belongs(unsolved_problems))

    rows = db(query).select(ptable.id,
                            orderby='<random>',
                            limitby=(0, stopstalk_constants.RECOMMENDATION_COUNT))

    return [x.id for x in rows]

def retrieve_past_recommendations(user_id):
    """
    Retrieve problems already recommended in the past for the given user.

    @param user_id (Integer): User ID for which recommendations need to be retrieved.
    @return (List, List): Problem IDs of the past active and inactive recommendations.
    """
    return generate_recommendations(user_id), []

def update_recommendation_status(user_id, problem_id, submission = None):
    """
    Update the status of the recommendation in the database.

    @param user_id (Integer): User ID for which status should be updated.
    @param problem_id (Integer): Problem ID for wich status should be updated.
    @param submission (Tuple): Problem submission.
    """
    return

def can_refresh_recommendations(user_id):
    """
    Check whether recommendations can be refreshed.

    @param user_id (Integer): User ID for which the check should be done.
    @return (Boolean): Flag to identify whether recommendations can be refreshed.
    """
    return True
