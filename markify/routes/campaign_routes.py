from flask import Blueprint

campaigns_bp = Blueprint('campaigns', __name__)

@campaigns_bp.route('/campaigns')
def list_campaigns():
    # Your route logic for listing campaigns
    pass