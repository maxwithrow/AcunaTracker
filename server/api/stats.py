from flask import Blueprint, request
import statsapi

stats = Blueprint('stats', __name__)

@stats.route('/')
def get_stats():
    acuna_id = statsapi.lookup_player('acuna')[0]['id']
    acuna_stats = statsapi.player_stat_data(acuna_id, group='hitting')['stats'][0]['stats']
    return {
        'homeruns': acuna_stats['homeRuns'],
        'stolenbases': acuna_stats['stolenBases']
    }