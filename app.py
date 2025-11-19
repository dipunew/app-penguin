from palmerpenguins import load_penguins
from plotnine import ggplot, aes, geom_histogram, theme_minimal
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from shiny.express import ui, render, input

# UI
ui.input_radio_buttons(
    id="species",
    label="Species",
    choices=["Adelie", "Gentoo", "Chinstrap"],
    inline=True,
)

# Load data
dat = load_penguins()

# Server
@render.plot
def plot():
    # Read selected species from UI
    sp = input.species()

    # Filter data reactively
    sel = dat.loc[dat.species == sp]

    # Plot
    return (
        ggplot(dat, aes(x="bill_length_mm"))
        + geom_histogram(data=dat, fill="#c2c2c4", alpha=0.7, binwidth=1)
        + geom_histogram(data=sel, fill="#447099", alpha=0.9, binwidth=1)
        + theme_minimal()
    )
