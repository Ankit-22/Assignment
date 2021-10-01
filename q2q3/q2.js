const superagent = require('superagent');
const cheerio = require('cheerio');

const titles = [];
let maxTitles = 10;


// Check if command line argument is provided and is valid
if(process.argv[2] && process.argv[2] <= maxTitles && process.argv[2] > 0) {
    maxTitles = process.argv[2];
} else if(process.argv[2]) {
    console.log("Please provide an limit between 1 to 10..");
    console.log(`Continuing with limit as ${maxTitles} for now..`);
}

// Get all the titles in box office by scraping html using cheerio
superagent.get("https://www.imdb.com/chart/boxoffice")
    .then((response) => {

        const $ = cheerio.load(response.text);
        castPromises = [];

        $(".titleColumn").each((i, data) => {
            // Select title only if limit is not reached
            if(i < maxTitles) {
                let title = {};
                title.id = $(data).find('a').attr('href').split('?')[0];
                title.name = $(data).text().trim();
                // Add a promise for cast details in a list
                castPromises.push(superagent.get("https://www.imdb.com" + title.id + "/fullcredits"));
                titles.push(title);
            }
        });

        // Wait for all cast details to be available
        Promise.all(castPromises).then((castDetails) => {
            castDetails.forEach((castDetail, index) => {
                titles[index].cast = [];
                let $$ = cheerio.load(castDetail.text);
                $$('.cast_list').find('tr.even, tr.odd').each((i, data) => {
                    titles[index].cast.push($(data).find('td:not(.primary_photo, .ellipsis, .character)').text().trim());
                });
            });

            // Print all the collected details
            console.log(titles);
        });
});