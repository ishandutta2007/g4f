import sys
import json
import urllib.parse

from curl_cffi import requests

config = json.loads(sys.argv[1])
messages = config['messages']
prompt = ''


def transform(messages: list) -> list:
    result = []
    i = 0

    while i < len(messages):
        if messages[i]['role'] == 'user':
            question = messages[i]['content']
            i += 1

            if i < len(messages) and messages[i]['role'] == 'assistant':
                answer = messages[i]['content']
                i += 1
            else:
                answer = ''

            result.append({'question': question, 'answer': answer})

        elif messages[i]['role'] == 'assistant':
            result.append({'question': '', 'answer': messages[i]['content']})
            i += 1

        elif messages[i]['role'] == 'system':
            result.append({'question': messages[i]['content'], 'answer': ''})
            i += 1
            
    return result

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Sec-Fetch-Mode': 'navigate',
    'Host': 'you.com',
    'Origin': 'https://you.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
    'Referer': 'https://you.com/api/streamingSearch?q=nice&safeSearch=Moderate&onShoppingPage=false&mkt=&responseFilter=WebPages,Translations,TimeZone,Computation,RelatedSearches&domain=youchat&queryTraceId=7a6671f8-5881-404d-8ea3-c3f8301f85ba&chat=%5B%7B%22question%22%3A%22hi%22%2C%22answer%22%3A%22Hello!%20How%20can%20I%20assist%20you%20today%3F%22%7D%5D&chatId=7a6671f8-5881-404d-8ea3-c3f8301f85ba&__cf_chl_tk=ex2bw6vn5vbLsUm8J5rDYUC0Bjzc1XZqka6vUl6765A-1684108495-0-gaNycGzNDtA',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Priority': 'u=0, i',
    'Cookie': 'uuid_guest=a98516de-c46a-40f6-abcb-40bbb00d9831; safesearch_guest=Moderate; youpro_subscription=false; ldflags=%7B%22abAppNavigationInChat%22%3A%22treatment%22%2C%22abCenterQueryBar%22%3A%22control%22%2C%22abCodeSnippetEmbeddingSearch%22%3A%22treatment%22%2C%22abCodeSnippetEmbeddingSearchV2%22%3A%22neither%22%2C%22abDegradationSwapTopAppWithBottomApp%22%3A%22neither%22%2C%22abDegradationSwapTopAppWithHighestWeb%22%3A%22neither%22%2C%22abDegradationSwapTopWebWithBottomWeb%22%3A%22neither%22%2C%22abDegradationSwapTopWebWithHighestApp%22%3A%22neither%22%2C%22abDegradeAppRankingForSomeIntents%22%3A%22neither%22%2C%22abEnableMultilingualLlm%22%3A%22control%22%2C%22abEnableMultilingualLlMv2%22%3A%22treatment%22%2C%22abFeaturedSnippet%22%3A%22control%22%2C%22abFormatYouChatResponses%22%3A%22control%22%2C%22abHomePageSearchToYouChat%22%3A%22treatment%22%2C%22abImagesWebResultsInChatReponse%22%3A%22neither%22%2C%22abLlmOrder%22%3A%22fastest_with_more_backup%22%2C%22abMakeDefaultSerpPageCta%22%3A%22treatment%22%2C%22abOnboardingMovieForGuests%22%3A%22control%22%2C%22abOneTapLogin%22%3A%22treatment%22%2C%22abOptimus%22%3A%22neither%22%2C%22abPersonalizationProfile%22%3A%22neither%22%2C%22abQuickAnswer%22%3A%22control%22%2C%22abReduceAppSearchTimeout%22%3A%22neither%22%2C%22abReduceNumApps%22%3A%22treatment%22%2C%22abRemoveBadUrlsV2%22%3A%22neither%22%2C%22abShowLandingPageGradient%22%3A%22neither%22%2C%22abShowSignInButton%22%3A%22treatment%22%2C%22abSkipNavigationalWebIfNotHighPrecision%22%3A%22neither%22%2C%22abSkipSearchForNonSearchIntent%22%3A%22treatment%22%2C%22abSportSurvey%22%3A%22neither%22%2C%22abStreamAppRankingsAfterApps%22%3A%22treatment%22%2C%22abSuggestedChatsV2%22%3A%22treatment%22%2C%22abThumbsAndDropdownAsSingleButton%22%3A%22control%22%2C%22abUseAppsForYouChat%22%3A%22treatment%22%2C%22abUseBraveAutoSuggest%22%3A%22neither%22%2C%22abUseBraveSearch%22%3A%22neither%22%2C%22abUseFalcon%22%3A%22treatment%22%2C%22abUseMultitaskLlm%22%3A%22treatment%22%2C%22abUseQueryRewriter%22%3A%22treatment%22%2C%22abUseRicherSnippetsForYouChat%22%3A%22treatment%22%2C%22abWebLinksStrip%22%3A%22neither%22%2C%22abYouChatCapGuest%22%3A%22cap_off%22%2C%22abYouChatPrivateAds%22%3A%22treatment%22%2C%22abYouChatResponseCap%22%3A0%2C%22abYouChatResponseCapV2%22%3A0%2C%22abYouPay%22%3A%22soft%22%2C%22abYouPayAlternatePricing%22%3A%22control%22%2C%22abYouProAnnouncementModalV2%22%3A%22treatment%22%2C%22abYouProButtonRedirection%22%3A%22neither%22%2C%22allowPremiumService%22%3A%22treatment%22%2C%22chatModelFlag%22%3A%22neither%22%2C%22controlUsedOpenAiModel%22%3A%22default%22%2C%22enableAppRankingV2%22%3Atrue%2C%22enableAppsFlyerWebSdk%22%3Afalse%2C%22enableAppsPreferences%22%3Atrue%2C%22enableBuySellAds%22%3A%22control%22%2C%22enableChatSpecificHeader%22%3Afalse%2C%22enableClaudeForFinance%22%3Afalse%2C%22enableFingerprint%22%3Afalse%2C%22enableLandingPageV3%22%3A%22control%22%2C%22enableMainAds%22%3A%22control%22%2C%22enableMinCitationsForYouChat%22%3A%22treatment%22%2C%22enableOneTapRepositioning%22%3Atrue%2C%22enableProfilePage%22%3Atrue%2C%22enableShopnomixYouChatAd%22%3Atrue%2C%22enableSponsoredWebResults%22%3A%22treatment%22%2C%22enableUpdateNativeAppAlert%22%3A%22none%22%2C%22enableYouAgent%22%3A%22neither%22%2C%22enableYouChatMobileNudge%22%3Atrue%2C%22llmOrder%22%3A%22fastest_with_more_backup%22%2C%22multitaskLlmEngineName%22%3A%22no_use%22%2C%22shouldShowYouChatRightLine%22%3Atrue%2C%22shouldUseStytchAuth%22%3Atrue%2C%22showSuggestedSearchPills%22%3Afalse%2C%22showYouchat%22%3A%22treatment%22%2C%22useAlternativeSearchInAllTab%22%3A%22treatment%22%2C%22useBingFallbackForAllTab%22%3A%22neither%22%2C%22useCacheForChatRetrieval%22%3A%22neither%22%2C%22useChatHistoryCache%22%3A%22treatment%22%2C%22usePermChatHistory%22%3A%22treatment%22%2C%22useYouChatConvoImageGen%22%3A%22control%22%2C%22validateUser%22%3A%22on%22%7D; cf_clearance=nOfK0HRl5kHBjqIITZTEnYZszICaK5hVm3HeERBjbyc-1690432619-0-1-fd246c9b.71c202a5.aa25337b-250.0.0; region=en-US; __cf_bm=R4Mq6hAHXq2ChB12z1NZaTTEwneL2kIq5IRLzA8NMdg-1690432869-0-ASk5PuVkSIoMdlKa1PFaz6jd5eD19Py2mdYLx6L8aQe+9/3rrLuwu1eBecYPLvrE2GUiVDjzsX5bZBbwaRh+m8WoSp7NG33Ps5qru5mpkNsL'
}

if messages[-1]['role'] == 'user':
    prompt = messages[-1]['content']
    messages = messages[:-1]

params = urllib.parse.urlencode({
    'q': prompt,
    'domain': 'youchat',
    'chat': transform(messages)
})

def output(chunk):
    if b'"youChatToken"' in chunk:
        chunk_json = json.loads(chunk.decode().split('data: ')[1])

        print(chunk_json['youChatToken'], flush=True, end = '')

while True:
    try:
        response = requests.get(f'https://you.com/api/streamingSearch?{params}',
                        headers=headers,content_callback=output,impersonate='safari15_5')
        exit(0)
    
    except Exception as e:
        print('an error occured, retrying... |', e, flush=True)
        continue