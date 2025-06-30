
import git

def revert_last_commit(repo_path):
    try:
        repo = git.Repo(repo_path)
        repo.git.revert('HEAD', no_edit=True)
        return "✅ تم التراجع عن آخر تعديل."
    except Exception as e:
        return f"❌ فشل التراجع: {e}"
