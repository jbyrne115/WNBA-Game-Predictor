import dash
from dash.dependencies import Input, Output
from dash import html
from dash import dcc
from nba_api.stats.endpoints import leaguegamefinder
import requests

gamefinder = leaguegamefinder.LeagueGameFinder(
    date_from_nullable='05/13/2023', league_id_nullable='10')
games = gamefinder.get_data_frames()[0]

team_names = games['TEAM_NAME'].unique()
team_names.sort()
team_name_dropdown_options = [{'label': i, 'value': i} for i in team_names]

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("WNBA Games Winner Prediction"),
    html.Label("Making predictions of WNBA matchups using the average plus-minus(+/-) of the previous 10 games for each team"),
    html.H2("Home Team"),
    dcc.Dropdown(
        id='home_team',
        options=team_name_dropdown_options,
        value=team_names[0]
    ),
    html.H2("Away Team"),
    dcc.Dropdown(
        id='away_team',
        options=team_name_dropdown_options,
        value=team_names[1]
    ),
    html.H3(id='output_text')
])


@app.callback(
    Output('output_text', 'children'),
    Input('home_team', 'value'),
    Input('away_team', 'value'),
)
def update_output_div(home_team, away_team):
    response = requests.get(
        'http://127.0.0.1:8000/predict_wnba_home_win/',
        params={'team_home': home_team,
                'team_away': away_team},
    )
    json_response = response.json()
    winning_team = home_team if json_response['result'] == 1 else away_team
    probability_of_winning = (json_response['win_probability']) * 100 if winning_team \
                                                                == home_team \
        else (1 - json_response['win_probability']) * 100

    probability_of_winning = round(probability_of_winning, 2)
    return f'{winning_team} has a ' f'{probability_of_winning}' '% chance to win the game.'



if __name__ == '__main__':
    app.run_server(debug=True)