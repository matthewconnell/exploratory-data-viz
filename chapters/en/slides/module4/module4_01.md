---
type: slides
---

# Visualizing Multidimensional Distributions

Notes: In this slide deck, we will extend what we learned in the
previous module about visualizing individual quantitative dataframe
columns as one-dimensional distributions to also be able to visualize
two-dimensional distributions.

---

## Reading in the data

``` python
import altair as alt
import pandas as pd

movies_extended = pd.read_csv('data/movies-extended.csv')
movies_extended
```

```out
                           Title    US Gross  Worldwide Gross  US DVD Sales  Production Budget Release Date MPAA Rating  Running Time min           Distributor                     Source        Major Genre         Creative Type         Director  Rotten Tomatoes Rating  IMDB Rating  IMDB Votes
0             Boynton Beach Club   3127472.0        3127472.0           NaN          2900000.0  Mar 24 2006           R             104.0  Wingate Distribution        Original Screenplay    Romantic Comedy  Contemporary Fiction              NaN                     NaN          NaN         NaN
1                   Broken Arrow  70645997.0      148345997.0           NaN         65000000.0  Feb 09 1996           R             108.0      20th Century Fox        Original Screenplay             Action  Contemporary Fiction         John Woo                    55.0          5.8     33584.0
2                         Brazil   9929135.0        9929135.0           NaN         15000000.0  Dec 18 1985           R             136.0             Universal        Original Screenplay       Black Comedy               Fantasy    Terry Gilliam                    98.0          8.0     76635.0
3                  The Cable Guy  60240295.0      102825796.0           NaN         47000000.0  Jun 14 1996       PG-13              95.0         Sony Pictures        Original Screenplay             Comedy  Contemporary Fiction      Ben Stiller                    52.0          5.8     51109.0
4                 Chain Reaction  21226204.0       60209334.0           NaN         55000000.0  Aug 02 1996       PG-13             106.0      20th Century Fox        Original Screenplay             Action  Contemporary Fiction     Andrew Davis                    13.0          5.2     15817.0
...                          ...         ...              ...           ...                ...          ...         ...               ...                   ...                        ...                ...                   ...              ...                     ...          ...         ...
1185                  Zombieland  75590286.0       98690286.0    28281155.0         23600000.0  Oct 02 2009           R              87.0         Sony Pictures        Original Screenplay             Comedy               Fantasy  Ruben Fleischer                    89.0          7.8     81629.0
1186  Zack and Miri Make a Porno  31452765.0       36851125.0    21240321.0         24000000.0  Oct 31 2008           R             101.0         Weinstein Co.        Original Screenplay             Comedy  Contemporary Fiction      Kevin Smith                    65.0          7.0     55687.0
1187                      Zodiac  33080084.0       83080084.0    20983030.0         85000000.0  Mar 02 2007           R             157.0    Paramount Pictures  Based on Book/Short Story  Thriller/Suspense         Dramatization    David Fincher                    89.0          NaN         NaN
1188         The Legend of Zorro  45575336.0      141475336.0           NaN         80000000.0  Oct 28 2005          PG             129.0         Sony Pictures                     Remake          Adventure    Historical Fiction  Martin Campbell                    26.0          5.7     21161.0
1189           The Mask of Zorro  93828745.0      233700000.0           NaN         65000000.0  Jul 17 1998       PG-13             136.0         Sony Pictures                     Remake          Adventure    Historical Fiction  Martin Campbell                    82.0          6.7      4789.0

[1190 rows x 16 columns]
```

Notes: We’re continuing to work with the movies data set. Here we have
done some additional preprocessing steps to to the data and saved it to
disk beforehand so that we can load it in directly on this slide.

This is largely the same dataset as before, but we filtered out some
additional NaNs and a few categories that contained problematic values.

---

## Scatter plots are effective visualizations for 2D distributions

``` python
alt.Chart(movies_extended).mark_point().encode(
    alt.X('IMDB Rating'),
    alt.Y('Rotten Tomatoes Rating'))
```

<iframe src="/module4/charts/01/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: In the last module we saw how to visualize the distribution of a
single numerical dataframe column. What if we instead want to compare
the distributions of two columns with each other?

A question we could answer with this type of comparison is “Are movies
rated similarly on different online platforms?”

In this slide we are showing the movie rating from both
<https://www.imdb.com/> and <https://www.rottentomatoes.com>. These are
both websites where people can rate movies.

There is clearly a pattern in this scatter plot, but how can we
interpret it?

The first thing that stands out is the overall pattern of the points
which is resembles a diagonal line with some variation around it.

When the points in a scatter plot lines up in a pattern that resembles a
diagonal line as in this chart, it means that the there is a
relationship between the two dataframe columns we have visualized.

In other words, we can clearly see that as one of the ratings goes up,
so does the other and there are only a few exceptions to this.

The relationship in this plot would be considered strong because we can
clearly the diagonal trend that the points follow.

---

## Non-linear relationships follow a predictable pattern that is not a straight line

``` python
alt.Chart(movies_extended).mark_point().encode(
    alt.X('IMDB Rating'),
    alt.Y('IMDB Votes'))
```

<iframe src="/module4/charts/01/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: The relationship in the previous slide followed a straight line
and we would refer to it as a “linear” relationship.

However, not all relationships are linear. In this slide we can see that
there appears to be a clear pattern between the rating and the number of
votes a movie receives but it follows a bent curve rather than a
straight line.

This still appears to be a pretty strong relationship, but it is a bit
hard to tell because of the many points in a big chunk at the bottom.

When a relationship is not following a straight line, we say that it is
non-linear. There are many types of non-linear relationships, but we
will not delve into them in course.

---

## The stronger the relationship, the closer together the points are

``` python
alt.Chart(movies_extended).mark_point().encode(
    alt.X('IMDB Rating'),
    alt.Y('IMDB Rating'))
```

<iframe src="/module4/charts/01/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: If the relationship between two column was really strong, the
points would be very close together and there would be little variation.

In this plot we have visualized the same column for both the X and Y
axis, which means the relationship is perfect.

We would never expect to see this strong of a relationship in real data,
but it is good to know what are the extreme cases.

On that topic, let’s see what a plot looks like when there appears to be
no relationship between the plotted dataframe columns.

---

## When there is no relationship, there is also no pattern in the plotted points

``` python
alt.Chart(movies_extended.reset_index()).mark_point().encode(
    alt.X('IMDB Rating'),
    alt.Y('index'))
```

<iframe src="/module4/charts/01/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Here, we have plotted the IMDB Rating against the row number in
the dataframe (remember that when you reset the index of a dataframe a
new column is created with the previous index / row number).

Unless the data had been ordered in a specific manner previously, we
would expect there to be no relationship between these two dataframe
columns and that is exactly what we see in this plot.

There is no distinct pattern here, just a cloud of points. In other
words, by knowing the value on the x-axis, there is no way we could know
the value on the y-axis.

For example, a movie with an IMDB Rating of 4-5 could have an index
number anywhere from 0 to 1200.

Let’s contrast this with the first visualization we created.

---

## A strong relationship means that the value on one axis gives information about the value on the other axis

``` python
alt.Chart(movies_extended).mark_point().encode(
    alt.X('IMDB Rating'),
    alt.Y('Rotten Tomatoes Rating'))
```

<iframe src="/module4/charts/01/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Here, knowing the IMDB Rating for a movie is informative for
knowing the Rotten Tomatoes Rating.

For example, if we know that the IMDB Rating is 4-5, we can be quite
sure that the Rotten Tomatoes Rating will not exceed 50, and there are
just a few exceptions to this.

However, we must be careful not to claim that there is a causal
relationship between these two dataframe columns. All we know is that
they have a strong relationship, we don’t know the details of why.

There are formal ways of measure how strong these relationships are, but
they often come with some caveats and it is generally more informative
to look at the visualizations to understand how the two columns are
related to each other.

Remember what we learned in module 1, people are generally better at
detecting visual patterns than interpreting individual numbers
summarizing these relationships.

---

## Saturated scatter plots are difficult to interpret

``` python
alt.Chart(movies_extended).mark_point().encode(
    alt.X('Production Budget'),
    alt.Y('Worldwide Gross'))
```

<iframe src="/module4/charts/01/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: As we have seen, scatter plots are generally effective for
visualizing two dimensional relationships. However, as with all plots,
they have their shortcomings.

Most notably, when the bulk of the points become concentrated to a small
region of the chart, 2D scatter plots become saturated in the same way
as the 1D scatter and rug plots we saw in the previous module.

In this slide we’re trying to answer the question: “Do high grossing
movies tend to have a high production budget?”

In the scatter plot you can see that it it is impossible to tell if
there are more points close to 80 million or 0 on the x-axis, and
likewise 200 million or 0 on the y-axis.

So although we can discern a trend for the points outside the saturated
area we do not know how they data is spread out inside the blue blob.

To solve this issue, we can create a two-dimensional histogram in the
form of a heatmap.

---

## A heatmap can visualize the relationship between two distributions without saturation

``` python
alt.Chart(movies_extended).mark_rect().encode(
    alt.X('Production Budget', bin=alt.Bin(maxbins=60)),
    alt.Y('Worldwide Gross', bin=alt.Bin(maxbins=60)),
    alt.Color('count()'))
```

<iframe src="/module4/charts/01/unnamed-chunk-8.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: What’s involved in creating a two-dimensional histogram?

This is similar to when we several heatmaps to compare multiple 1D
distributions, but here we need to bin both the x and y-axis.

These bins will look like a grid or mesh overlayed on the image, similar
to the pattern of the faint grey gridlines in the previous slide.

Within each rectangle of this grid, we will count the number of
observations and represent the count value with a color.

The result of these operations is the heatmap shown in this slide, which
enables us to see a level of detail we could not perceive in the scatter
plot.

Here it is clear that there are many fewer movies with a production
budget of 80 million compared to the area close to 0, and most movies
seem to be around 10-15 million. Likewise the grossing of most movies is
around 0-50 million, not 200 million.

---

## A 2D density plot can also visualize the relationship between two distributions without saturation

<img src="/module4/unnamed-chunk-5-1.png" width="48%" />

Notes: In addition to representing 2D distributions as heatmaps, we can
also represent them as density plots.

Altair cannot yet make these plots, so here we’re showing an example
created from another plotting library called seaborn, so that you can
get a sense of what this visualization would look like for our data.

In a 2D density plot, each bin is now two dimensional and look like a
bell in a clocktower or the top of a circus tent, rather than a
bell-shaped one-dimensional curve.

This type of visualization gives us similar information as the heatmap
in the previous slide and the advantages and disadvantages are similar
to those between one-dimensional histograms and density plots.

As with 1D density plots, the values of the density themselves are not
helpful, but we have included them here in the colorbar as an example.

---

# Let’s apply what we learned!

Notes: <br>