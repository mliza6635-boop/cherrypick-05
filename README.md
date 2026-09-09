# Lab 5: Cherry-pick — Move One Important Fix

Starter file:
- `config_check.py` — contains a bug: it does NOT check whether `APP_ENV` exists.

Follow the tasks in the assignment sheet:
1. Create `hotfix-config` from `main`.
2. Fix `config_check.py` so it checks whether `APP_ENV` exists, and exits with status 1 when missing, e.g.:
   ```python
   if not app_env:
       print("Error: APP_ENV is not set")
       exit(1)
   print("Configuration OK")
   ```
3. Test with and without `APP_ENV` set:
   - `python3 config_check.py`
   - `APP_ENV=dev python3 config_check.py`
4. Commit the fix and find the commit ID with `git log --oneline -1`.
5. Switch to `main`, create `feature-report`.
6. Cherry-pick the hotfix commit: `git cherry-pick <commit-id>`.
7. Test again and view history with `git log --oneline --graph --all`.
