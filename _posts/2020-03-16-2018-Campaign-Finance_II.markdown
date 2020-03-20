---
layout: post
title: "Campaign Finance 2018, Part II: A closer look"
date: 2020-03-16 16:00:00 -0400
comments: true
category: blog
tags: ["FEC", "campaign finance", "2018 elections", "data science", "EDA"]
---
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The &#8594;[first post](https://blog.volsweep.com/blog/2019/12/12/2018-Campaign-Finance_I.html)&#8592; in this series was an overview of trends and exceptions in Congressional midterm contests with respect to party affiliation, incumbency status, and relative funding status. To recap: incumbents usually lead fundraising and win.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This post will be a more in-depth look at the &#8594;[full set of data](https://www.fec.gov/data/browse-data/?tab=bulk-data)&#8592; that the FEC publishes.  As before, all relevant code is in &#8594;[this](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018)&#8592; GitHub repo.[^1]


### "House/Senate current campaigns"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one candidate ID per row. This is the one we used to construct the plots in the first post of this series, showing relative candidate fundraising status by contest. We know from this set the following breakdown of the top three contest "types" for each branch of Congress:

*2018 U.S. Senate contests*
* 58.8% had a Democratic incumbent ahead in fundraising,
* 8.8% had a Republican incumbent ahead in fundraising,
* 8.8% had a Republican challenger ahead in fundraising.

*2018 U.S. House of Representatives contests*
* 30.8% had a Republican incumbent ahead in fundraising,
* 24.0% had a Democratic incumbent ahead in fundraising,
* 14.6% had a Democratic incumbent running unopposed.


### "Candidate-committee linkages"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one row per candidate-committee pairing (NB it does not contain committees that are not linked to candidates). You can see the ones linked to at least three candidates, including candidate info, by searching "list starts here" on [this page]. The following candidates are linked to more than ten committees in this data set: Tammy Baldwin, Sherrod Brown, Joe Donnelly, Heidi Heitkamp, Amy Klobuchar, Claire McCaskill, Bill Nelson, Jacky Rosen, Debbie Stabenow, and Jon Tester.


### "Committee master"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one row per committee. After deduplication of several columns, we found there are some treasurers associated with large numbers of committees, and some addresses associated with large numbers of committees. Search the phrase, "look here," in &#8594;[this](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/03a%20-%202018_CommitteeMaster_clean.ipynb)&#8592; notebook for a breakdown by address and treasurer (e.g., Lisa Lisker, Keith Davis, and David Satterfield are the treasurers of a very large number of committees located at 228 S Washington St, Alexandria, VA 22314).


### "Contributions from committees to candidates & independent expenditures"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one contribution/independent expenditure per row. The different types of contributions/independent expenditures are:

* "contribution made to nonaffiliated committee,"
* "independent expenditure advocating election of candidate,"
* "independent expenditure opposing election of candidate,"
* "in-kind contribution made to registered filer,"
* "coordinated party expenditure,"
* "election recount disbursement,"
* "communication cost against candidate (only for Form 7 filer)."

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During the cleaning process before plotting, we made some observations. First of all, Invenergy PAC made 691 contributions and/or independent expenditures with no date given (only 3 additional had a date). Embraer Aircraft Holding Inc PAC made 154 contributions and/or independent expenditures with no date given. The Democratic Senatorial Campaign Committee (DSCC) received $306,644 total in contributions with no individuals' names given. The National Republican Senatorial Committee (NRSC) received $294,519 total in contributions with no individuals' names given.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Each plot below shows, for one source each, independent expenditures **advocating** and **opposing** individual candidates. Let's go through them one by one.

**Bully Pulpit Interactive**


**Connection Strategy**[^1]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There is no active trace of Connection Strategy online; it appears no longer to be in business. It advocated for Republicans only, except for one Democrat running for an open seat and four more Democrats whom Connection Strategy also opposed.

**Facebook**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Facebook is interesting because it made the most independent expenditures _both_ advocating and opposing individual candidates. See how crowded the middle area of that plot is? No other plot looks like that for 2018. Additionally, we see that the majority of Facebook independent expenditure funds _advocating_ a candidate were made with respect to _Democratic_ candidates, whereas the majority of independent expenditure funds _opposing_ a candidate were made with respect to _Republican_ candidates.

**Prolist**[^6]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Prolist has a similar spending profile to Connection Strategy but with a higher average dollar expenditure. It was founded in 1989, and according to its "About" page:

> *"...We also have expanded to focus on database management, fundraising efforts for nonprofits and other organizations, digital integration, political campaign marketing through our ProTarget service, and so much more ... From Intelligent Mail to integrated email marketing and digital fulfillment, ProList continues to make history as the model for direct marketing services companies of the twenty-first century."*

**SKDKnickerbocker**[^7]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Before the 2018 midterms, SKDKnickerbocker was acquired by the Stagwell Group, which was founded by former Microsoft chief Steven A. Ballmer and is headed by Mark Penn[^8]. We see from the plot that it made independent expenditures purely advocating for Democrats only, and most of those were challengers. It made independent expenditures both advocating and opposing one Republican incumbent. SKDKnickerbocker's independent expenditures purely opposing candidates focused on Republicans (mostly incumbents) with the exception of a Democratic incumbent.

**Waterfront Strategies**


<div class="clearfix">

  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/ie_BullyPulpitInteractive.png">
      <img alt="Bully Pulpit Interactive" src="{{ site.url }}/assets/FECpt2/ie_BullyPulpitInteractive.png" style="width: 100%">
    </a>
  </div>

  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/ie_ConnectionStrategy.png">
      <img alt="Connection Strategy" src="{{ site.url }}/assets/FECpt2/ie_ConnectionStrategy.png" style="width: 100%">
    </a>
  </div>

  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/ie_Facebook.png">
      <img alt="Facebook" src="{{ site.url }}/assets/FECpt2/ie_Facebook.png" style="width: 100%">
    </a>
  </div>
</div>

<div class="clearfix">

  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/ie_Prolist.png">
      <img alt="Prolist" src="{{ site.url }}/assets/FECpt2/ie_Prolist.png" style="width: 100%">
    </a>
  </div>

  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/ie_SKDKnickerbocker.png">
      <img alt="SKDK" src="{{ site.url }}/assets/FECpt2/ie_SKDKnickerbocker.png" style="width: 100%">
    </a>
  </div>

  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/ie_WaterfrontStrategies.png">
      <img alt="Waterfront Strategies" src="{{ site.url }}/assets/FECpt2/ie_WaterfrontStrategies.png" style="width: 100%">
    </a>
  </div>

</div>


### Contributions by individuals

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one contribution from an individual per row. We had to do a lot of cleaning in this set in particular. Any names containing "anonymous", "unitemized", and/or anything like "hat pass" we switched to simply "Anonymous." The FEC rules state:

> *"An anonymous contribution of cash is limited to $50. Any amount in excess of $50 must be promptly disposed of and may be used for any lawful purpose unrelated to any federal election, campaign or candidate." [^9]*

This doesn't seem to be the case, as $246,892 total across two contributions to Composition Roofers Local Union #30 PAC and $54,458 total across two contributions to Association for Firefighters PAC. These appear to be above the limits allowed by the FEC.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In cleaning the state abbreviations column, we found some that do not match those of U.S. states or territories: AE, AP, FM, ZZ, MH, AA, PW, and null. A lot of the FM ones appear to be Florida cities; a lot of the ZZ ones appear to be cities in foreign countries; most of the null ones are U.S. cities and the state abbreviation is just missing. We left these as-is for now as they only constitute ~0.2% of total observations. The reason why the state abbreviation per observation is important is that we want to distinguish between in-state contributions/independent expenditures and out of state ones.


**U.S. Senate, Florida**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_FLsenate_committee.png">
      <img alt="FLsenate_committee" src="{{ site.url }}/assets/FECpt2/contributions_FLsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_FLsenate_individual.png">
      <img alt="FLsenate_individual" src="{{ site.url }}/assets/FECpt2/contributions_FLsenate_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. Senate, Indiana**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_INsenate_committee.png">
      <img alt="INsenate_committee" src="{{ site.url }}/assets/FECpt2/contributions_INsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_INsenate_individual.png">
      <img alt="INsenate_individual" src="{{ site.url }}/assets/FECpt2/contributions_INsenate_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. Senate, Missouri**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_MOsenate_committee.png">
      <img alt="MOsenate_committee" src="{{ site.url }}/assets/FECpt2/contributions_MOsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_MOsenate_individual.png">
      <img alt="MOsenate_individual" src="{{ site.url }}/assets/FECpt2/contributions_MOsenate_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. Senate, North Dakota**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_NDsenate_committee.png">
      <img alt="NDsenate_committee" src="{{ site.url }}/assets/FECpt2/contributions_NDsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_NDsenate_individual.png">
      <img alt="NDsenate_individual" src="{{ site.url }}/assets/FECpt2/contributions_NDsenate_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. Senate, New Jersey**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_NJsenate_committee.png">
      <img alt="NJsenate_committee" src="{{ site.url }}/assets/FECpt2/contributions_NJsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_NJsenate_individual.png">
      <img alt="NJsenate_individual" src="{{ site.url }}/assets/FECpt2/contributions_NJsenate_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. Senate, Nevada**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_NVsenate_committee.png">
      <img alt="NVsenate_committee" src="{{ site.url }}/assets/FECpt2/contributions_NVsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_NVsenate_individual.png">
      <img alt="NVsenate_individual" src="{{ site.url }}/assets/FECpt2/contributions_NVsenate_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. Senate, Texas**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_TXsenate_committee.png">
      <img alt="TXsenate_committee" src="{{ site.url }}/assets/FECpt2/contributions_TXsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_TXsenate_individual.png">
      <img alt="TXsenate_individual" src="{{ site.url }}/assets/FECpt2/contributions_TXsenate_individual.png" style="width: 100%">
    </a>
  </div>
</div>

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_CA21_committee.png">
      <img alt="CA21_committee" src="{{ site.url }}/assets/FECpt2/contributions_CA21_committee.png" style="width: 100%">
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
      <img alt="FL26_committee" src="{{ site.url }}/assets/FECpt2/contributions_FL26_committee.png" style="width: 100%">
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
      <img alt="GA06_committee" src="{{ site.url }}/assets/FECpt2/contributions_GA06_committee.png" style="width: 100%">
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
      <img alt="IL06_committee" src="{{ site.url }}/assets/FECpt2/contributions_IL06_committee.png" style="width: 100%">
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
      <img alt="MI09_committee" src="{{ site.url }}/assets/FECpt2/contributions_MI09_committee.png" style="width: 100%">
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
      <img alt="OK05_committee" src="{{ site.url }}/assets/FECpt2/contributions_OK05_committee.png" style="width: 100%">
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
      <img alt="PA08_committee" src="{{ site.url }}/assets/FECpt2/contributions_PA08_committee.png" style="width: 100%">
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
      <img alt="UT04_committee" src="{{ site.url }}/assets/FECpt2/contributions_UT04_committee.png" style="width: 100%">
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
      <img alt="VA10_committee" src="{{ site.url }}/assets/FECpt2/contributions_VA10_committee.png" style="width: 100%">
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
      <img alt="VA11_committee" src="{{ site.url }}/assets/FECpt2/contributions_VA11_committee.png" style="width: 100%">
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
      <img alt="WI01_committee" src="{{ site.url }}/assets/FECpt2/contributions_WI01_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_WI01_individual.png">
      <img alt="WI01_individual" src="{{ site.url }}/assets/FECpt2/contributions_WI01_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**Footnotes**

[^1]: Cleaning notes to consider: 1) only data pertaining to candidates appearing on final ballots remain, and 2) any candidate not affiliated with one of the two major parties has been categorized as, "Third party."
[^1]: https://www.clubforgrowth.org/
[^2]: Dead link: http://www.connectionstrategy.com/
[^3]: https://www.i-360.com/
[^4]: https://www.politico.com/story/2014/12/koch-brothers-rnc-113359
[^5]: https://www.opensecrets.org/news/2019/01/political-consultants-making-millions-to-influence-elections/
[^6]: https://www.prolist.com/about-prolist/
[^7]: https://www.skdknick.com/
[^8]: https://www.nytimes.com/2015/10/09/business/dealbook/stagwell-group-will-acquire-skdknickerbocker.html
[^9]: https://www.fec.gov/help-candidates-and-committees/candidate-taking-receipts/contribution-limits/
