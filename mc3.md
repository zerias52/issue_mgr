# Mini Challenge 3
## Issue Management
### Acceptance Criteria
1. Run your server and create a product owner account (a user whose role is product owner).
2. Create `urlpatterns` and `templates` for the following views:
2.1. IssueListView
2.1.1. This should be a "board" with 3 columns. A column for "to do", one for "in progress" and one for "done".
2.2. IssueDetailView
2.3. IssueUpdateView
2.4. IssueDeleteView
2.5. IssueCreateView
2.5.1. Remember: only product owners can use this (so hide it from non-product owners).
3. Test!
## Bonus (extra points)
Make it so that issues can be transitioned between columns easily (up to you how).
Suggestions: javascript that issues a POST request to the update view, or a simple form can work as well.