import CovidDataService

class App:
    def __init__(self, plotter):
        self.plotter = plotter
        
    def run(self):
        covid_data = CovidDataService()
        data = covid_data.get_countries_data(['Mexico', 'USA'])
        self.plotter.plot_data(data)