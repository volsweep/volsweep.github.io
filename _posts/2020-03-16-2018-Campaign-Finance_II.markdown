---
layout: post
title: "Campaign Finance 2018, Part II: A closer look"
date: 2020-03-16 16:00:00 -0400
comments: true
category: blog
tags: ["FEC", "campaign finance", "2018 elections", "data science", "EDA"]
---
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*TL;DR*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The &#8594;[first post](https://blog.volsweep.com/blog/2019/12/12/2018-Campaign-Finance_I.html)&#8592; in this series on 2018 campaign finance filings with the Federal Election Commission (FEC) was an overview of trends and exceptions with respect to party affiliation, incumbency status, and relative funding status. To recap: incumbents are usually ahead in fundraising and win. For contests where the incumbent is not ahead in fundraising (excludes open seat contests), there is a threshold between $3-5MM above which challengers are more likely to win. In 2018's case, these were mostly Democratic-affiliated challengers; it remains to be seen how this pattern generalizes across midterm vs. general elections, for example.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This post will be more of an in-depth examination of the &#8594;[full set of data](https://www.fec.gov/data/browse-data/?tab=bulk-data)&#8592; that the FEC makes available.  As before, all relevant code is in &#8594;[this](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018)&#8592; GitHub repo.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Some cleaning notes to consider: 1) only data pertaining to candidates appearing on final ballots remain, and 2) any candidate not affiliated with one of the two major parties has been categorized as, "third party." Now we'll go through the FEC data sets one by one in the order we processed them.


### House/Senate current campaigns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one candidate ID per row. This is the one we used to construct the plots in the first post of this series, showing relative candidate fundraising status by contest. We know from this set the following breakdown of the top three contest "types" for each branch of Congress:

*2018 U.S. Senate contests*
* 58.8% had a Democratic incumbent ahead in fundraising,
* 8.8% had a Republican incumbent ahead in fundraising,
* 8.8% had a Republican challenger ahead in fundraising.

*2018 U.S. House of Representatives contests*
* 30.8% had a Republican incumbent ahead in fundraising,
* 24.0% had a Democratic incumbent ahead in fundraising,
* 14.6% had a Democratic incumbent running unopposed.


### Candidate-committee linkages

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one line per candidate-committee pairing (NB it does not contain committees that are not linked to candidates). You can see the ones linked to at least three candidates, including candidate info, by searching "list starts here" on [this page]. The following candidates are linked to more than ten committees in this data set: Tammy Baldwin, Sherrod Brown, Joe Donnelly, Heidi Heitkamp, Amy Klobuchar, Claire McCaskill, Bill Nelson, Jacky Rosen, Debbie Stabenow, and Jon Tester.


### Committee master

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one line per committee. After deduplication of several columns, we found there are some treasurers associated with large numbers of committees, and some addresses associated with large numbers of committees. For example:


_Treasurers pertaining to over 50 committees_

_(format: Full name, Number of committees (Number of committees linked to a candidate))_

* **Paul Kilgore**, 144 (27)
* **Christopher Marston**, 122 (11)
* **Judith Zamore**, 109 (53)
* **Lisa Lisker**, 88 (14)
* **Jennifer May**, 62 (15)
* **Benjamin Ottenhoff**, 56 (4)
* **Jay Patterson**, 56 (20)


_Addresses pertaining to more than 100 committees, treasurers listed_

* **228 S Washington St, Alexandria, VA 22314** (156 committees)

  * David Satterfield
  * Francis Kirley
  * Greg Laughlin
  * John Dwyer
  * Keith Davis
  * Larry Steinberg
  * Lisa Lisker
  * Taylor Moose


* **918 Pennsylvania Ave AE, Washington, D.C. 20003** (112 committees)

  * Aaron Watson
  * Amy Eckert
  * Ellen Tauscher
  * Halle Mayes
  * Judith Zamore
  * Karen Mascott
  * Kristin Solander
  * Megan Mielnik
  * Melissa Nissen
  * Michael Schrum


* **824 S Milledge Ave, Athens, GA 30605** (101 committees)

  * Greg Mosing
  * Megan Brown
  * Michael Goode
  * Paul Kilgore


### Contributions from committees to candidates & independent expenditures

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one contribution/independent expenditure per row. The different types of contributions/independent expenditures are:

* "contribution made to nonaffiliated committee,"
* "independent expenditure advocating election of candidate,"
* "independent expenditure opposing election of candidate,"
* "in-kind contribution made to registered filer,"
* "coordinated party expenditure,"
* "election recount disbursement,"
* "communication cost against candidate (only for Form 7 filer)."

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During the cleaning process before plotting, we made some observations. First of all, Invenergy PAC made 691 contributions and/or independent expenditures with no date given (only 3 additional had a date). Embraer Aircraft Holding Inc PAC made 154 contributions and/or independent expenditures with no date given. The Democratic Senatorial Campaign Committee (DSCC) received $306,644 total in contributions with no individuals' names given. The National Republican Senatorial Committee (NRSC) received $294,519 in contributions with no individuals' names given.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Each plot below shows, for one source each, independent expenditures **advocating** and **opposing** individual candidates. For example, Club for Growth made independent expenditures around $100 advocating for the Democratic challenger shown as a blue diamond in the middle of the Club for Growth plot, and about $1000 opposing the same candidate. (The axes are a log scale base 10, so the 1 axis marker means 10<sup>1</sup> = $10, the 2 means 10<sup>2</sup> = $100, the 3 means 10<sup>3</sup> = $1,000, and so on.) Let's go through these one by one.

**Club for Growth**[^1]

According to its website, "Club for Growth is a national network of over 250,000 pro-growth, limited government Americans who share in the belief that prosperity and opportunity come from economic freedom." We can see from the plot that it advocates for incumbent, challenger, and open seat Republicans, and opposes fewer of the same plus some Democrats, as well. The three symbols in the center area of the plot represent two open seat Republicans and one Democratic challenger, all of whom were both advocated and opposed by Club for Growth via independent expenditures.

**Connection Strategy**[^2]

There is no active trace of Connection Strategy online; it appears no longer to be in business. It advocated for Republicans only, except for one Democrat running for an open seat and the four more Democrats whom Connection Strategy also opposed.

**Facebook**

Facebook is interesting because it made the most independent expenditures _both_ advocating and opposing individual candidates. See how crowded the middle area of that plot is? No other plot looks like that for 2018. Additionally, we see that the majority of Facebook independent expenditure funds _advocating_ a candidate were made with respect to _Democratic_ candidates, whereas the majority of independent expenditure funds _opposing_ a candidate were made with respect to _Republican_ candidates.

**Google**

Google didn't spend nearly as much money on independent expenditures in 2018 as Facebook did. Two incumbents, one from each major party, had a combination of advocating and opposing funds spent by Google; most of the purely advocated candidates were Democrats but the ratio is closer to even than Facebook's.

**I360**[^3]

According to its website, "Our team of data scientists build and refine proven, sophisticated models that enable us to predict behaviors and actions, such as the likelihood to support or oppose an issue, redeem a coupon, subscribe to an email list, or even purchase a particular brand or product. This knowledge is powerful, informing messaging and enhancing your ability to target and reach the right customer to achieve success at scale." It is funded by Koch family money[^4]. It spend up to about $100,000 each advocating Republicans/opposing Democrats. It spent advocating and opposing funds with respect to one Republican incumbent.

**Nebo Media**

OpenSecrets had as much difficulty as we did finding an online presence for Nebo Media; there isn't one[^5]. Its independent expenditure dollar amounts are pretty high compared to others shown here; up to ~$1MM advocating individual Republican candidates and almost $10MM opposing some Democratic candidates. Interestingly, there is a lone Republican candidate whom Nebo Media opposed.

**Prolist**[^6]

Prolist has a similar spending profile to Connection Strategy but with a higher average dollar expenditure. It was founded in 1989, and according to its "About" page:

> "...We also have expanded to focus on database management, fundraising efforts for nonprofits and other organizations, digital integration, political campaign marketing through our ProTarget service, and so much more ... From Intelligent Mail to integrated email marketing and digital fulfillment, ProList continues to make history as the model for direct marketing services companies of the twenty-first century."

**SKDKnickerbocker**[^7]

Before the 2018 midterms, SKDKnickerbocker was acquired by the Stagwell Group, which was founded by former Microsoft chief Steven A. Ballmer and is headed by Mark Penn[^8]. We see from the plot that it made independent expenditures purely advocating for Democrats only, and most of those were challengers. It made independent expenditures both advocating and opposing one Republican incumbent. In terms of independent expenditures purely opposing candidates, SKDKnickerbocker focused on Republicans (mostly incumbents) with the exception of a Democratic incumbent.

**United States Postal Service (USPS)**

Interestingly, USPS independent expenditures purely advocating for candidates are pretty mixed by party compared to other plots we've seen, but we definitely notice that the higher amounts went with respect to Republican incumbents. In terms of independent expenditures purely opposing candidates, again, the party split is relatively even but USPS appears to oppose several incumbent Democrats in particular. USPS: not a fan of incumbent Democrats?



<div class="clearfix">
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_committee_ClubForGrowth.png">
      <img alt="Club For Growth" src="{{ site.url }}/assets/FECpt2/contributions_committee_ClubForGrowth.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_committee_ConnectionStrategy.png">
      <img alt="Connection Strategy" src="{{ site.url }}/assets/FECpt2/contributions_committee_ConnectionStrategy.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_committee_Facebook.png">
      <img alt="Facebook" src="{{ site.url }}/assets/FECpt2/contributions_committee_Facebook.png" style="width: 100%">
    </a>
  </div>
</div>
<div class="clearfix">
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_committee_Google.png">
      <img alt="Google" src="{{ site.url }}/assets/FECpt2/contributions_committee_Google.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_committee_I360.png">
      <img alt="I360" src="{{ site.url }}/assets/FECpt2/contributions_committee_I360.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_committee_NeboMedia.png">
      <img alt="Nebo Media" src="{{ site.url }}/assets/FECpt2/contributions_committee_NeboMedia.png" style="width: 100%">
    </a>
  </div>
</div>
<div class="clearfix">
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_committee_Prolist.png">
      <img alt="Prolist" src="{{ site.url }}/assets/FECpt2/contributions_committee_Prolist.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_committee_SKDKnickerbocker.png">
      <img alt="SKDKnickerbocker" src="{{ site.url }}/assets/FECpt2/contributions_committee_SKDKnickerbocker.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_committee_USPS.png">
      <img alt="USPS" src="{{ site.url }}/assets/FECpt2/contributions_committee_USPS.png" style="width: 100%">
    </a>
  </div>
</div>


### Contributions by individuals

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one contribution from an individual per row. We had to do a lot of cleaning in this set in particular. Any names containing "anonymous", "unitemized", and/or anything like "hat pass" we switched to simply "Anonymous." The FEC rules state:

> "An anonymous contribution of cash is limited to $50. Any amount in excess of $50 must be promptly disposed of and may be used for any lawful purpose unrelated to any federal election, campaign or candidate." [^9]

This doesn't seem to be the case, as $246,892 total across two contributions to Composition Roofers Local Union #30 PAC and $54,458 total across two contributions to Association for Firefighters PAC. These appear to be above the limits allowed by the FEC.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In cleaning the state abbreviations column, we found some that do not match those of U.S. states or territories: AE, AP, FM, ZZ, MH, AA, PW, and null. A lot of the FM ones appear to be Florida cities; a lot of the ZZ ones appear to be cities in foreign countries; most of the null ones are U.S. cities and the state abbreviation is just missing. We left these as-is for now as they only constitute ~0.2% of total observations. The reason why the state abbreviation per observation is important is that we want to distinguish between in-state contributions/independent expenditures and out of state ones.

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_CA21_committee.png">
      <img alt="CA21_commitee" src="{{ site.url }}/assets/FECpt2/contributions_CA21_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_CA21_individual.png">
      <img alt="CA21_individual" src="{{ site.url }}/assets/FECpt2/contributions_CA21_individual.png" style="width: 100%">
    </a>
  </div>
</div>

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_FL26_committee.png">
      <img alt="FL26_commitee" src="{{ site.url }}/assets/FECpt2/contributions_FL26_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_FL26_individual.png">
      <img alt="FL26_individual" src="{{ site.url }}/assets/FECpt2/contributions_FL26_individual.png" style="width: 100%">
    </a>
  </div>
</div>

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_GA06_committee.png">
      <img alt="GA06_commitee" src="{{ site.url }}/assets/FECpt2/contributions_GA06_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_GA06_individual.png">
      <img alt="GA06_individual" src="{{ site.url }}/assets/FECpt2/contributions_GA06_individual.png" style="width: 100%">
    </a>
  </div>
</div>

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_IL06_committee.png">
      <img alt="IL06_commitee" src="{{ site.url }}/assets/FECpt2/contributions_IL06_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_IL06_individual.png">
      <img alt="IL06_individual" src="{{ site.url }}/assets/FECpt2/contributions_IL06_individual.png" style="width: 100%">
    </a>
  </div>
</div>

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_MI09_committee.png">
      <img alt="MI09_commitee" src="{{ site.url }}/assets/FECpt2/contributions_MI09_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_MI09_individual.png">
      <img alt="MI09_individual" src="{{ site.url }}/assets/FECpt2/contributions_MI09_individual.png" style="width: 100%">
    </a>
  </div>
</div>

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_OK05_committee.png">
      <img alt="OK05_commitee" src="{{ site.url }}/assets/FECpt2/contributions_OK05_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_OK05_individual.png">
      <img alt="OK05_individual" src="{{ site.url }}/assets/FECpt2/contributions_OK05_individual.png" style="width: 100%">
    </a>
  </div>
</div>

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_PA08_committee.png">
      <img alt="PA08_commitee" src="{{ site.url }}/assets/FECpt2/contributions_PA08_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_PA08_individual.png">
      <img alt="PA08_individual" src="{{ site.url }}/assets/FECpt2/contributions_PA08_individual.png" style="width: 100%">
    </a>
  </div>
</div>

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_UT04_committee.png">
      <img alt="UT04_commitee" src="{{ site.url }}/assets/FECpt2/contributions_UT04_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_UT04_individual.png">
      <img alt="UT04_individual" src="{{ site.url }}/assets/FECpt2/contributions_UT04_individual.png" style="width: 100%">
    </a>
  </div>
</div>

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_VA10_committee.png">
      <img alt="VA10_commitee" src="{{ site.url }}/assets/FECpt2/contributions_VA10_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_VA10_individual.png">
      <img alt="VA10_individual" src="{{ site.url }}/assets/FECpt2/contributions_VA10_individual.png" style="width: 100%">
    </a>
  </div>
</div>

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_VA11_committee.png">
      <img alt="VA11_commitee" src="{{ site.url }}/assets/FECpt2/contributions_VA11_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_VA11_individual.png">
      <img alt="VA11_individual" src="{{ site.url }}/assets/FECpt2/contributions_VA11_individual.png" style="width: 100%">
    </a>
  </div>
</div>

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_WI01_committee.png">
      <img alt="WI01_commitee" src="{{ site.url }}/assets/FECpt2/contributions_WI01_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_WI01_individual.png">
      <img alt="WI01_individual" src="{{ site.url }}/assets/FECpt2/contributions_WI01_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**Footnotes**

[^1]: https://www.clubforgrowth.org/
[^2]: Dead link: http://www.connectionstrategy.com/
[^3]: https://www.i-360.com/
[^4]: https://www.politico.com/story/2014/12/koch-brothers-rnc-113359
[^5]: https://www.opensecrets.org/news/2019/01/political-consultants-making-millions-to-influence-elections/
[^6]: https://www.prolist.com/about-prolist/
[^7]: https://www.skdknick.com/
[^8]: https://www.nytimes.com/2015/10/09/business/dealbook/stagwell-group-will-acquire-skdknickerbocker.html
[^9]: https://www.fec.gov/help-candidates-and-committees/candidate-taking-receipts/contribution-limits/
