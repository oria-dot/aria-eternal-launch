# strategic_dashboard.py – Fixed

def render_clone_status(clones):
    for cid, role in clones.items():
        print(f"{cid}: {role}")
