---
type: slides
---

# Exploratory Data Analysis on Categorical Data

Notes: To perform EDA on categorical data we look at the counts of
observations for each of the categories, as we have learned previously.

---

## A statistical summary is useful to complement visualizations

``` python
import pandas as pd

movies_extended = pd.read_csv('data/movies-extended-eda.csv')
movies_extended.describe(exclude='number')
```

```out
       Major Genre         Creative Type MPAA Rating
count         1196                  1191        1193
unique          12                     8           4
top         Comedy  Contemporary Fiction       PG-13
freq           286                   640         486
```

Notes: Since we have already seen the dataset rows and info in the last
slide deck, we start by describing the data here.

In addition to generally receiving more information about our data,
categorical counts are helpful when building machine learning
classification models. Having an unbalanced data set for the dataframe
column we are trying to predict (i.e., uneven numbers of things in the
various categories) would mean that we need to compensate for this in
our downstream analysis.

There are many other examples in statistical analysis, where uneven
categories can change how you need to do your analysis. Failing to
account for this would lead to less accurate and possibly misleading
results.

As for the numerical columns above, we start by printing information
about the most frequently occurring categorical values in each of the
columns. We use `exclude` to indicate that we want to use all other
columns except the numerical ones.

We can already here see what the most commons values are for each
column, but let’s visualize these in a bar chart and cross-reference
this table with our plot on the next slide.

---

## Visualizing the counts of all categorical columns helps us understand the data

``` python
import altair as alt

categorical_columns = movies_extended.select_dtypes('object').columns.tolist()
(alt.Chart(movies_extended)
 .mark_bar().encode(
     alt.X('count()'),
     alt.Y(alt.repeat(), type='nominal', sort='x'))
 .properties(width=200, height=150)
 .repeat(categorical_columns))
```

<iframe src="/module4/charts/12/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To answer how the counts are distributed between different
categorical vaules, we will create a bar chart for each categorical
dataframe column.

The syntax here is very similar to when we created the histograms, but
we don’t use any bins, and the axis type is now nominal instead of
quantitative.

We can see that most movies are dramas and comedies, and fall withing
the R and PG-13 ratings. Our plot for the titles look horrible because
there is not enough room to plot one line per title.

We could have included the title column here to check that no two movies
have the same title. After that we can safely skip that subplot since it
is rather messy with all the hundreds titles.

However, since this is EDA and not a plot created for communication, we
could also have left it in and carried on.

---

## Repeat can also be used to explore the counts of combinations of categorical columns

``` python
(alt.Chart(movies_extended).mark_circle().encode(
     alt.X(alt.repeat('column'), type='nominal', sort='-size'),
     alt.Y(alt.repeat('row'), type='nominal', sort='size'),
     alt.Color('count()', title=None),
     alt.Size('count()', title=None))
 .repeat(row=categorical_columns, column=categorical_columns)
 .resolve_scale(color='independent', size='independent'))
```

<iframe src="/module4/charts/12/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: The same repeat principles can be used to count combinations of
categoricals, helping us get more resolution into where the data lies.

This plot should be read similarly to the pairplot we made earlier, so
ony look at the three plots below the diagonal.

In this plot we can see that Contermporary Comedies, as well as comedies
rated PG-13 and dramas rated R are the most common combinations in our
data.

In the fact, there are so many more of these than some of the others
that we should be careful if we proceed to perform any statistical tests
on this data as many such tests are not robust against samples sizes
that are this unequal and we need to adapt our testing strategy
accordingly.

---

## Altair’s grammar allows us to repeat facetted charts

``` python
(alt.Chart(movies_extended.query('`MPAA Rating` == ["G", "R"]'))
 .mark_boxplot().encode(
     alt.X('Running Time min', type='quantitative'),
     alt.Y(alt.repeat('row'), type='nominal'),
     alt.Color('MPAA Rating'))
 .facet(column='MPAA Rating')
 .repeat(row=['Major Genre', 'Creative Type']))
```

<iframe src="/module4/charts/12/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Thanks to the flexible grammar of graphics in Altair, we are able
to repeat complex charts, such as those already containing facets.

In this case, we are interested in comparing the counts of the Major
Genres and Create Types within each of the `G` and `R` MPAA RAtings.

To achieve this, we first facet the chart and then repeat it, combing
the principles we have learned so far in the course.

Now we can answer questions such as which the most popular genres are
within each of the ratings.

As we might have expected, the top genres differs depending on the MPAA
Rating, and there are many genres that are not even present for the
famiy rated G movies.

---

# Let’s apply what we learned!

Notes: <br>