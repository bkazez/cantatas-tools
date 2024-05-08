#!/opt/homebrew/bin/python3.9

# import the OpenAI Python library for calling the OpenAI API
from pprint import pprint
import openai
import random

def sample_lines(s, n=450):
    lines = s.split('\n')
    return '\n'.join(random.sample(lines, min(n, len(lines))))

MODEL = "gpt-3.5-turbo"
openai.api_key_path = "openai_api_key.txt"

user = """
youth
worldly vanity
worldly transience
worldly temptation
worldly possessions
worldly disillusionment
worldly desires
world's rejection
world renunciation
wonder
willing death
wealth in poverty
weakness
victory over sin
victory of savior
value
unworthiness
unrepentance
trust in jesus
trust in god's mercy
tribute
tribulation
transience
transformation through love
transcendence of physical death
total dedication
territorial boundaries
surrender
sun
suffering to joy
submission to god's will
stubbornness
strength
steadfastness
spiritual victory
spiritual union with christ
spiritual thirst
spiritual sweetness
spiritual strength
spiritual security
spiritual satisfaction
spiritual resurrection
spiritual purity
spiritual protection
spiritual journey
spiritual growth
spiritual gifts
spiritual fruitfulness
spiritual elevation
spiritual distress
spiritual diligence
spiritual death and rebirth
spiritual caution
spiritual battle
sowing tears
soul's purity
soul's contentment
sorrow relief
son of god
societal norms
social interaction
sinners
sincerity
shepherd metaphor
shared joy
selflessness
self-sufficiency
self-love
self-improvement
satan's deception
safety
royalty
righteous living
reversal of fortunes
reverence
resistance to evil
resistance
remembrance of god's work
religious zeal
religious martyrdom
relief
rejuvenation
rejection of earthly honor
rejection
readiness for heaven
quelling divine wrath
queen
purity
pride
preparation
prayer in jesus' name
prayer for mercy
praising the trinity
praise for savior
poverty
plea for safety
plea for patience
personal suffering
peaceful rest
peace on earth
peace in afterlife
peace amidst chaos
path to life
overcoming satan
overcoming poverty
original sin
omnipresence
new year
new life
new beginnings
neighborly love
muses
morning star
mockery
misguided faith
miracles
melody
marital bliss
love for neighbor
light
lifelong devotion
life-death struggle
leadership
law
lamentation
lament
lack of peace
lack of mercy
knowledge of living jesus
kingdom of god
justification
judgement day
joyful worship
joyful faith
joy in death
joy in adversity
joy after suffering
john 14:23
jesus' victory
jesus' suffering
jesus' resurrection
jesus' protection
jesus' name
jesus' humility
jesus' ascension
jesus' arrival
jesus as shepherd
jesus as savior
jesus as refuge
jesus as mediator
jesus as bridegroom
israel
inner turmoil
inner conflict
immortality
humble hearts
human will
human suffering
human limitation
human folly
hope in suffering
holy dwelling
heavenly vision
heavenly peace
heavenly inheritance
heavenly hope
heavenly ascension
heaven
heart's purity
heart as god's dwelling
hardened hearts
hard-heartedness
guidance of the holy spirit
gossip
good deeds
golden age
god's thoughtfulness
god's sovereignty
god's righteousness
god's poverty
god's justice
god's glory
god's eternity
god's creation
god's blessings
god as shepherd
god
glory to god
future glory
fulfillment of prophecy
friendship
fortune
fearlessness in death
fearlessness
fear of loss
fear of judgement
fear of death
faithful servitude
faithful heart
faithful devotion
faith path
faith in suffering
faith in god's word
faith in god's will
faith in god's plan
faith in death
faith community
faith and salvation
expulsion of sin
eternal wealth
eternal life with christ
eternal kingdom
eternal gratitude
eternal goodness
eternal damnation
eternal commitment
enduring hardship
endurance in trials
emotional appeal
embrace of savior
elevation
echo
easter lamb
earthly events
divine visitation
divine vision
divine throne
divine teaching
divine support
divine sovereignty
divine son
divine shepherd
divine satisfaction
divine salvation
divine reward
divine retribution
divine purpose
divine pleasure
divine path
divine omnipresence
divine joy
divine hearing
divine fatherhood
divine covenant
divine communication
divine blessings
divine assurance
divine approval
disciples' fear
desire for heavenly union
desire for heavenly joy
desire for heaven
departure
demonstration of love
deceit
death's fear
death without fear
death as liberation
death and afterlife
day and night
darkness
danger
cross
courage in faith
contentment in faith
complete joy
comfort in suffering
comfort in sorrow
comfort in jesus
comfort in god's word
comfort in god
comfort in faith
comfort in christ
coffee love
christian virtues
christian patience
christian life
christian identity
christian burial
christ's sacrifice
christ's call
christ's birth
christ as lamb of god
charity
care
burning love
brotherly love
blessing of leadership
blessed land
blessed christians
biblical quote
baptismal vow
awakening
avoidance of sin
aspiration
appreciation
angelic transformation
angelic presence
angelic joy
angelic guidance
agriculture
zion's blessings
youthfulness
yearly blessings
wrathful enemies
worldly vs heavenly focus
worldly vs divine glory
worldly suffering
worldly success
worldly sorrow
worldly sin
worldly power
worldly persecution
worldly indifference
worldly honor
worldly escape
worldly disgust
worldly deception
worldly decay
world's transience
world's sorrow
world's end
world's destruction
world's corruption
world rejection
world conquest
world as a hospital
word of life
word of grace
word and truth
witness for christ
wisdom of christ
wisdom in leadership
wine drinking
wind
willingness for death
wickedness of the world
wickedness
wholehearted and soulful commitment
well-wishing
well-being
welcoming the final hour
welcoming death
wedding celebration
weapons
wealth of soul
wealth
weak faith
wavering faith
watchmen
warning against hypocrisy
walking god's path
waiting
voice
vocal preparation
virtue over material wealth
virgin mary
village life
vigilant shepherd
victory through jesus
victory over satan
victory over enemies
victory of life
victory of belief
victory in god
victory in faith
victorious savior
verbal expression
vanity of worldly desires
vanity of earthly riches
vanity
value of simplicity
value of god's word
urban life
unyielding love
unwavering trust
unrequited love
unpreparedness
unparalleled love
unmerciful judgment
unleashing of fury
universal reach
unity with god
unity of mind
unity of hearts
unity in faith
unity in christ
union with the lamb
union with god
union with christ
unexpected end
unexpected blessings
unending torment
unending joy
undisturbed affection
understanding of sacrifice
understanding faith
uncountable blessings
uncorrupted word of god
unchanging commitment
uncertainty of life
uncertainty
unbreakable love
unbound singing
unassailable faith
unasked prayers
unanswered prayers
tyranny
two souls
truthfulness
truth and peace
trust in the creator
trust in god's power
trust in god's plan
trust in god's goodness
true light
true confession
troubles
triumphant christ
triumph
transient wealth
transient suffering
transience of the world
transformative suffering
transformation into joy
transfiguration
transcendence
tranquility
tired of the world
timelessness
time perception
thwarting evil
threat of war
thorny spiritual path
thirst
thanksgiving to god
text_themes
ten commandments
temporary abandonment
temporality
taxation
tavern setting
tavern
taste of savior's goodness
taste of divine goodness
sustenance
survival
surrender to jesus
surrender of worries
suffering for salvation
suffering as growth
suffering and joy
suffering and comfort
sudden death
sudden change
successful strategy
successful execution
success
submission under god
submission to christ
submission
struggle and resistance
struggle against flesh
struggle
strong love
striving for goodness
strengthening of the church
strength in weakness
strength in sorrow
strength in song
strength in joy
straying path
storytelling
storm of life
storm
steadfastness in troubled times
steadfastness in faith
steadfast belief
standing on the brink of eternity
spring winds
spiritual zion
spiritual wellness
spiritual wealth in jesus
spiritual weakness
spiritual warning
spiritual upliftment
spiritual understanding
spiritual treasure
spiritual sustenance
spiritual steadfastness
spiritual slumber
spiritual resistance
spiritual relief
spiritual reign of christ
spiritual refreshment
spiritual rebirth
spiritual reassurance
spiritual purification
spiritual preparedness
spiritual preparation
spiritual poverty
spiritual peace
spiritual path
spiritual pain
spiritual memory
spiritual learning
spiritual illness
spiritual ignition
spiritual hunger
spiritual humility
spiritual health
spiritual gratitude
spiritual freedom
spiritual dwelling
spiritual duty
spiritual discernment
spiritual despair
spiritual desire
spiritual defense
spiritual dedication
spiritual deception
spiritual decay
spiritual cultivation
spiritual complacency
spiritual cleansing
spiritual attachment
spiritual aspiration
spiritual and physical nourishment
spiritual acceptance
spending
sowing for eternity
sowing blessings
sowing and reaping
soul's wealth
soul's waiting
soul's trust
soul's treasure
soul's torment
soul's sun
soul's suffering
soul's struggle
soul's salvation
soul's reunion with body
soul's preparation
soul's joy
soul's immortality
soul's distress
soul's delight
soul's anguish
soul revival
soul purification
soul offering
soul in jesus' hands
soul as paradise
soul
songwriting
song contest
song composition
song
solitude
social responsibility
social hierarchy
sleeping worries
sinners' purification
singing praises
sinful nature
sinful destruction
sinful desires
sinful birth
sincerity of heart
sin's torment
sin's stain
sin's origin
sin's filth
sin's corruption
sin's consequences
sin washing
sin renunciation
sin redemption
sin recognition
sin eradication
sin confession
sin burial
sin burden
sin bearing
sin bearer
sin avoidance
sin atonement
sin and sorrow
sin and redemption
sin and guilt
sin against god
sin acknowledgment
silent suffering
sheep's safety
sharing
shared wishes
shared celebration
service to savior
service to others
service to neighbor
servant of god
servant leadership
servant
separation from world
separation from god
separation anxiety
sensory pleasure
self-transcendence
self-satisfaction
self-questioning
self-praise
self-knowledge
self-judgement
self-imposed challenge
self-destruction
self-confidence
self-condemnation
self-awareness of sin
self-accusation
self-abasement
seeking wisdom
seeking salvation
seeking refuge
seeking peace
seeking help
seeking god
seeking freedom
seeking divine wisdom
search for god
search for fulfillment
sea storm
scripture
scholar
saxony's wellbeing
saxony's welfare
saxony's protection
saxony
saxon hero's life
savior's role
saving
satisfaction
satanic envy
satan's wrath
satan's opposition
sarmatia
sanctity
sanctified mind
sanctified dwelling
sanctification of souls
samaritan-like hearts
samaritan
salvation through faith and baptism
salvation teaching
salvation for the chosen
salvation by faith
sacrificial lamb
sacrifice on the cross
sacred festivity
sacrament of communion
sacrament
sabbath observance
rural life
royal lineage
royal dispute
royal blessings
royal benevolence
roses and thorns metaphor
romans 2:4–5
role model
river symbolism
river personification
river nymphs
river metaphor
river imagery
righteousness through faith
righteous judgement
right path
right faith
richness in poverty
rich herds
reward of virtue
reward of hard work
reward of diligence
revelation through scripture
revelation
return to earth after death
return to earth
retribution
resurrection through christ
resurrection of jesus
resurrection of christ
resurrection belief
resurrection as consolation
rest in god
respect
resisting worldly distractions
resisting sin
resistance to sin
resilience in love
resilience in adversity
repentance and forgiveness
renunciation of the world
renunciation
renewed light
renewed hope
renewal of faith
remembrance of jesus' sacrifice
remembrance
religious sincerity
religious praise
religious persecution
religious instrumental chorale
relief from sin
relief from pain
relief from earthly suffering
reliance on jesus
reliance on god's grace
reliance on divine comfort
rejuvenation through melody
rejection of worries
rejection of worldly treasures
rejection of worldly ties
rejection of worldly temptations
rejection of worldly desires
rejection of world
rejection of the false world
rejection of the accuser
rejection of suffering
rejection of material offerings
rejection of idols
rejection of grace
rejection of false teachings
rejection of earthly temptations
rejection of christ
regret of self-reliance
refuge in jesus
refuge
reflection
redemption through the lamb
redemption through jesus
redemption through christ
redemption through baptism
redemption from sin
red cheeks metaphor
recovery
reconciliation with god
reconciliation between god and humans
recognition of jesus
recognition of christ
reciprocity
reciprocal mercy
reciprocal love
rebellion
reassurance
readiness for mortality
readiness for death
quiet and godly life
questioning
queen's fame
purity of faith
purification through faith and baptism
pure faith
punishment for disobedience
public perception
public mourning
psalm 146:5
psalm 146:10
psalm 146:1
psalm 104
psalm 103:2
protection of the weak
protection of the flock
protection of the faithful
protection of faith
protection of believers
protection from temptation
protection from jesus christ
protection from disaster
protection from calamity
protection for christians
protection against misfortune
prosperous life
propriety
prophetic fulfillment
prophecy
promised relief
promise of heavenly joy
promise of change
procrastination
proclamation of miracles
proclamation of god's deeds
proclamation of christ
princely glory
prince leopold
prince as pan
priestly blessing
preservation of faith
prepared rest
preparation for the bridegroom
preparation for messiah
preparation for jesus
preparation for christ
prayer's power
prayer for strength
prayer for representation
prayer for protection
prayer for divine protection
prayer for divine help
prayer for divine guidance
prayer for church
prayer for a good end
praising god
praised field
praise to trinity
praise to the lord
praise to jesus
praise through jesus
praise of lord
praise of creation
praise for divine strength
praise and singing
praise and honor
practicing love
practice of mercy
practice of compassion
power of truth
power of jesus' name
power of jesus' blood
power of god's word
power of devotion
possessive love
pleissenstadt
pleasure and joy
pleasing sacrifices
pleasant sound
plea to zephyrus
plea to jesus
plea to god
plea to aeolus
plea for renewal
plea for recognition
plea for preservation
plea for peace
plea for hope
plea for grace
plea for gentleness
playful criticism
planting in the land
physical weakness
physical suffering
physical restoration
physical health
physical decline
phoebus
persuasion
personal well-being
personal merit
perfection
penance
peasant life
peaceful year
peaceful transformation
peaceful surrender
peaceful living
peaceful departure
peaceful christ
peace through jesus
peace request
peace offering
peace in salvation
peace in grave
peace in god's care
peace in death
peace and joy in heaven
patient waiting
patience under suffering
patience and hope
path to joy
path seeking
path of salvation
path of honor
path for jesus
pastoral imagery
pastoral duties
pastoral care
passionate thoughts
passion of christ
passing time
parting sorrow
parental frustration
parental control
parental blessing
parental authority
parental approval
parent-child conflict
paradise reopening
pan
pales' sacrifice
overwhelming sorrow
overwhelming joy
overcoming suffering
overcoming sin and death
overcoming sin
overcoming hardship
overcoming fear of death
overcoming evil
overcoming enemies
overcoming adversity
overcoming adversaries
outward piety
outer beauty of sin
origin of love
openness to god
openness to divine word
opening hearts
open-hearted confession
open-handedness
open heart
one god, three persons
omnipotence
old ways
old self dying
old age
offering soul to jesus
offering of heart to jesus
offering
obligation to rejoice
obedience to god's word
obedience to commandments
oath of allegiance
nourishment through faith
nourishment from god's word
nobility of spirit
nobility
no redemption
night-time questioning
night-time contemplation
night watch
newborn jesus
new year's resolution
new year's hope
new year's gift to jesus
new year's devotion
new year prayer
new world
new life in faith
new life in christ
new creation
new covenant
nature's testimony
nature and grace
natural devastation
national distress
national blessing
narrow path
name change
mydas
mutual understanding
mutual love
musical value
musical tribute
musical skill
musical prowess
musical metaphor
musical joy
musical instruments
musical harmony
musical competition
music's sorrow
music's power
music as praise
music appreciation
mother's death
moses' law
mortality awareness
moral choice
monetary metaphor
monarch's deeds
mockery of faith
misunderstood art
misunderstanding of disciples
misunderstanding
missing essential part
misfortune
military pride
midnight hour
metaphorical insects
messiah
merciful heart
memory
melodious joy
matthew 6
matthew 20:14
"""

user2 = """
martyrdom
marriage proposal
marriage negotiation
marital unity
marital union
marital joy
marital harmony
marital bond
manifest happiness
luke 2:49
luke 24:29
loyalty to king
love's fruition
love practice
love over force
love of jesus
love of god
love of christ
love for immanuel
love for enemies
love and happiness
love and faith
love against fate
loud singing
lost souls
loss of spiritual power
loss of jesus
loss of hope
loss and gain
lord's praise
longing for wings
longing for spiritual perfection
longing for salvation
longing for revelation
longing for relief
longing for peace
longing for liberation
longing for jesus' solace
longing for death and eternal life
long life
loneliness
local places
living by god's laws
living according to god's word
linden trees
limitless love
light over darkness
light of life
light of divine word
light of comfort
light in death
light for the heathens
life sustenance
life journey
life dedication
life
liberation from suffering
liberation from earthly imperfections
liberation
leopold's virtues
leopold's reign
legacy
left-handedness
law and gospel
laughter
late years
land's joy
land without leader
lack of spiritual growth
lack of self-sufficiency
kyrie eleis
knowledge
kings from saba
king's grave
king of kings
king of glory
justification through jesus
justice and peace
justice and faithfulness
judgment on lukewarm faith
judgment day
joyous sacrifice
joyous proclamation
joyous duty
joyful year
joyful rays
joyful moments
joyful hours
joyful harvest
joyful expectation
joyful entry
joyful defiance
joy to sorrow
joy through tribulation
joy of angels
joy in worship
joy in sorrow
joy in salvation
joy in resurrection
joy in heaven
joy in forgiveness
joy in christ
joy from god
joy for israel
joy and sorrow
joy and prosperity
joy and pleasure
journey to the grave
journey to salem
journey to jesus
journey to heaven
journey
john the baptist
john 16:20
jewish persecution
jesus' word
jesus' voice
jesus' teachings
jesus' sleep
jesus' return
jesus' redemption
jesus' passion
jesus' mercy
jesus' mediation
jesus' loss
jesus' life
jesus' journey
jesus' invitation
jesus' guidance
jesus' grace
jesus' gifts
jesus' fulfillment
jesus' embrace
jesus' departure
jesus' delight
jesus' companionship
jesus' comforting power
jesus' comfort
jesus' birth
jesus' appearance
jesus' acceptance of sinners
jesus' acceptance
jesus christ as hope
jesus as true wealth
jesus as treasure
jesus as shield
jesus as peace prince
jesus as life's purpose
jesus as life's light
jesus as joy
jesus as intercessor
jesus as friend
jesus as first and last
jesus as eternal soulmate
jesus as eternal glory
jesus as death's antidote
jesus as confidence
jesus as comfort
jesus as a healer
jesus alleviates suffering
jesting hearts
jerusalem's praise
jerusalem journey
jeremiah 5:3
jealousy
israel's liberation
isolation
isaiah's prophecy
irreplaceability
invocation of aeolus
inviting jesus
invitation
introspection
intercession
integrity
insufficiency of human efforts
instability
inner tranquility
inner reflection
inner purity
inner pride
inner pearls of satisfaction
inner emptiness
innate gifts
injustice
inheritance
ingratitude
infinite god
inevitable end
inevitability of death
inescapable divine justice
indwelling of god
indulgence
indifference to suffering
indifference of the beloved
inconstancy
incomprehensible omnipresence
incarnation of christ
inability to self-save
inability to resist sin
imperfection
imminent death
imminence of death
immanuel
imitation of god
illusion
ignorance
idolatry
idol rejection
identity as god's children
humility of god
humbling the proud
humble praise
humble offerings
humble gift
human wickedness
human vanity
human transformation
human sinfulness
human resistance
human rebellion
human misery
human lust
human life
human joy
human inability to achieve righteousness
human impatience
human ignorance
human heart
human fragility
human dissatisfaction
human depravity
human condition
human alienation
house of israel
house of aaron
hospitality
hope in pain
hope in jesus
hope in israel
hope in faith
hope in christ
hope for salvation
hope for mercy
hope for heavenly joy
hope for heavenly harvest
hope for future
hope for brighter future
hope and joy
hope after hardship
honoring authority
honor to saxon hero
honor to god
honor in death
honesty as divine gift
homage
holy zion
holy word
holy spirit's teaching
holy spirit's presence
holy spirit's gifts
holy spirit's assistance
holy spirit's arrival
holy praise
holy living
holy fire
holy community
holy communion
holy adoration
high well-being
heroic death
heresy
herald
hellish fear
hellfire
hell's silence
heavy sorrow
heavy misfortune
heavenly wedding feast
heavenly wealth
heavenly union
heavenly treasures
heavenly sweetness
heavenly selection
heavenly riches
heavenly reunion
heavenly return
heavenly rejoicing
heavenly praise
heavenly origin
heavenly life
heavenly kinship
heavenly kingdom
heavenly joy and freedom
heavenly homecoming
heavenly harmony
heavenly guidance
heavenly gate
heavenly focus
heavenly feast
heavenly faith
heavenly enthronement
heavenly election
heavenly dwelling
heavenly destiny
heavenly desire
heavenly descent
heavenly contentment
heavenly comfort
heavenly city
heavenly army
heavenly access
heaven's value
heaven's testimony
heaven and hell
heaven and earth
heartfelt singing
heartfelt prayer
heartfelt offering
heartfelt emotion
heart's surrender
heart's openness
heart's kiss
heart's faith
heart's dwelling
heart's devotion to god
heart's devotion
heart's corruption
heart's comfort
heart as fertile ground
heart as dwelling
heart as currency
health
healing through jesus' wounds
healing through harmony
healing through god's word
healing through faith
healing power of jesus
healing power
healing from inherited and personal sin
harsh overseer
harsh judgement for denial
hardship
hardness of heart
hardening of hearts
happiness
hallelujah
habsburg lineage
guidance through life
guidance of god
guardianship
grief
greenery
great commission
gratitude towards leadership
gratitude for wise leadership
gratitude for the past year
gratitude and duty
granting of power
grace for the repentant
grace beyond works
grace and mercy
grace and life
gospel comfort
goodwill towards men
good works
good governance
good ending
golden sun
golden rule
golden era
gold, incense, myrrh
gold and incense
gods
godly love
godlessness
god's work
god's word as truth
god's word
god's wonders
god's voice
god's vigilance
god's victory
god's timing
god's strength
god's purpose
god's protection and justice
god's promises
god's promise of goodness
god's proclamation
god's presence
god's power and holiness
god's power
god's plan
god's perfect will
god's perfect timing
god's patience
god's omnipotence
god's majesty
god's love for the world
god's longing
god's law
god's kingdom
god's judgement
god's increase
god's image
god's hidden will
god's guidance
god's greatness
god's gifts
god's generosity
god's friendship
god's evidence
god's eternal reward
god's endless goodness
god's embrace
god's elevation
god's dwelling
god's distance
god's daily goodness
god's daily blessings
god's compassionate heart
god's command
god's care
god's blessing
god's ascension
god's absence
god of jacob
god as sun and shield
god as protector
god as love
god as judge
god as giver
god as friend
god as fortress
god as eternal king
god as ally
glory
glorification of god
gloria patri
gloria in excelsis deo
gifts from saba
gifts for jesus
gift of life's word
german virtues
genuine piety
generosity
generational habits
gathering in jesus' name
future reward
futility of worry
fulfillment of wishes
fulfillment of vows
fulfillment of law
fulfillment of god's will
fulfillment of duty
fruitlessness
fruitful marriage
fruitful land
fruitful labor
frugality
friendliness
freedom from sin
freedom
fratricide
foundation of salvation
fortune's fickleness
forgotten legacy
forgiveness of enemies
forgetting god
foolishness
following god
following christ's example
following christ
focus on god
flutes
flourishing knowledge
floral symbolism
flora
flesh and spirit conflict
flesh and blood
fleeting pleasure
fleeting life
fleeting joy
fleeting existence
flattery
fire
finding jesus
finding god in loss
filial relationship with god
fiery hearts
fields and meadows
fervent faith
fervent devotion
fertility
fearlessness in faith
fearlessness in adversity
fearless testimony
fearless death
fear of the lord
fear of sin
fear of punishment
fear of judgment
fear of hypocrisy
fear of eternity
fear of denial
fear of daylight
fear of aeolus
fear of abandonment
fear not
fear and sin
fear and joy in faith
fear and hope
fear and faith
fear and doubt
farewell to worldly chaos
farewell to the world
familial conflict
fame
false wealth
false teachings
false prophets
false piety
false happiness
faithfulness to god
faithful soul
faithful shepherd
faithful service
faithful servants
faithful longing
faithful following
faithful endurance
faithful death
faithful community
faith, prayer, patience
faith's strength
faith's reward
faith's preparation
faith's journey
faith vs reason
faith under attack
faith testing
faith struggle
faith reinforcement
faith protection
faith preservation
faith over works
faith journey
faith inheritance
faith in word
faith in trials
faith in sorrow
faith in savior
faith in salvation
faith in resurrection
faith in prayer
faith in god's presence
faith in god's grace
faith in divine stone
faith in divine guidance
faith in divine goodness
faith in darkness
faith in christ's sacrifice
faith crisis
faith assurance
faith and trust
faith and righteousness
faith and love
faith and life
faith and hope
faith amidst suffering
faith amidst distress
face-to-face with god
extinguishing of divine light
expression of love
expression of faith
expression
exploitation
expansion
exclusive devotion to god
exaltation
evil hindrance
evening prayer
european suffering
ethical conduct
eternal word of christ
eternal unity
eternal union with god
eternal triumph
eternal suffering
eternal steadfastness
eternal standing
eternal service
eternal security
eternal satisfaction
eternal sabbath
eternal reign
eternal punishment
eternal preservation
eternal peace
eternal love for god
eternal life in jesus
eternal judgement
eternal hope
eternal harvest
eternal happiness
eternal freedom
eternal flame
eternal fire
eternal father
eternal death
eternal covenant
eternal companionship
eternal care
escape from worries
escape from sin
equality
envy and jealousy
enhancement of glory
enemy defeat
endymion
enduring name
enduring joy
enduring fame
enduring faith
enduring belief
endurance of suffering
endurance in hardship
endurance
endless suffering
end of life
encouragement in distress
encouragement
empty words
empathy for others
empathy
emotional release
emotional pain
emotional music
emotional healing
emotional distress
emotion
embracing suffering
effort in life
eden
echo of admiration
easter joy
easter feast
earthly vs divine light
earthly treasures
earthly temptations
earthly gold rejection
earthly glory
earthly despair
earth's life
eager for death
eager expectation
duty of gratitude
duke's peace and blessings
drinking suggestion
drinking
divine-human union
divine-human marriage
divine worthiness
divine worship
divine welcome
divine watchfulness
divine uniqueness
divine union
divine truth
divine trust
divine triumph
divine touch
divine testing
divine sustenance
divine surrender
divine stone
divine solidarity
divine solace
divine signs
divine shelter
divine service
divine selection
divine search
divine scrutiny
divine savior
divine sacrifice
divine reliability
divine rejection
divine refuge
divine redemption
divine record
divine reconciliation
divine recognition
divine reckoning
divine reassurance
divine pursuit
divine purification
divine preservation
divine omnipotence
divine nourishment
divine mission
divine miracles
divine mandate
divine majesty
divine love and grace
divine love and faithfulness
divine lineage
divine light in storms
divine kingship
divine inspiration
divine indwelling
divine image
divine hunting
divine hope
divine holiness
divine hiddenness
divine healing
divine gifts
divine gift
divine gentleness
divine foundation
divine forgiveness
divine focus
divine flame
divine fishing
divine exaltation
divine eternity
divine election
divine discipline
divine creation
divine courage
divine counsel
divine coronation
divine control
divine contemplation
divine constancy
divine consolation
divine consecration
divine commandment
divine command
divine choice
divine chastisement
divine champion
divine blood
divine birthright
divine authority
divine attraction
divine attention
divine assistance in conflict
divine and human favor
divine action
divine accompaniment
distress
distraction from faith
disobedience to god's command
disobedience
diligence
difficult journey
dialogue with pomona and pallas
dialogue between soprano and bass
dialogue between soprano and alto
devotion to jesus
devotion to god
devotion to christ
devil's temptation
devil's influence
detachment from world
detachment from wealth
destruction of evil
destination
desperation
despair and hope
desolation
desire to give heart to god
desire to end earthly life
desire for rest
desire for offspring
desire for divine presence
desire for divine intervention
desire for divine guidance
desire for death without jesus' love
desire for cooling
desecration of holy places
dependence on god
denial of christ
deliverance from suffering
deliverance
delayed assistance
defiance of limits
defiance of hell and death
defiance against enemies
defense of faith
defeat without god's presence
defeat of satan
defeat of evil
deep distress
deep calling
decision-making
debt
death's mockery
death's inevitability
death's fearlessness
death's desire
death's defeat
death's abyss
death wish
death in jesus
death in faith
death defeat
death as relief
death and resurrection of jesus
death and resurrection
death and faith
death and closure
death acceptance
day's joy
day of judgement
davidic lineage
darkness and light
dance
damnation
daily sin
daily renewal
daily dependence on god
curse of sin
crucifixion
crown of life
crown
cross journey
cross and crown
creator's abundance
creator
creativity
covering of sin
covenant
courtship
courage in suffering
counting hours
cosmic upheaval
conversion of heathens
conversion
control over nature
contentment in suffering
contentment in simplicity
contentment in poverty
contentment in god
contemplation of hell
contemplation
constant trials
constant sinfulness
constant focus on god
constant divine presence
constancy in suffering
constancy
consolation in christ
conflict
confidence in god
confidence amidst adversity
confidence
confession of sins
concept of uncountable time
completion of year
completion of the year
completion
complete victory
comparison to abel
companionship
community
communion
communal prayer
communal happiness
command to winds
comfort in adversity
collective well-wishing
collective joy
coffee renunciation
coffee obsession
coffee drinking
coffee as bargaining chip
coffee
cleansing from sin
cleansing by blood
cleansing
civic duty
city's glory
church's growth
church support
church corruption
church community
church bells
christianity
christian testimony
christian suffering
christian struggle
christian steadfastness
christian resilience
christian poverty
christian love
christian leadership
christian journey
christian hypocrisy
christian faith
christian duty
christian discipleship
christian courage
christian compassion
christian community
christian comfort
christian celebration
christian apostasy
christ-like heart
christ's victory
christ's suffering
christ's salvation
christ's righteousness
christ's reverence
christ's return
christ's protection
christ's miracles
christ's joy
christ's humility
christ's honor
christ's guidance
christ's exaltation
christ's divinity
christ's baptism
christ's ascension
christ as shepherd
christ as savior
christ as life
christ as cornerstone
christ as comfort
chosen souls
chosen christians
chosen christian
choice
children's blessing
childlike trust
childlike love
cherubim absence
chaste love
charitable deeds
character description
cessation of tears
cessation of mourning
celestial revelation
celestial bodies
celestial beings
celebration of victory
celebration of augustus
caution
casting off worries
captivity
cannons
call to love
call to live with jesus
call to believers
burning love for jesus
burden of sin
burden
broken vows
bridegroom's arrival
breaking boundaries
body's decay
body decay
body and soul care
blooming fields
blood's cleansing power
blood power
blood covenant
blindness to others' faults
blessing request
blessing on land and city
blessing on children
blessing in marriage
blessing in hardship
blessing in all ends
blessing for leaders
blessing for land
blessing for authorities
blessing abundance
blessed proclamation
blessed flock
bitter tears
birthday
birth of savior
birth of jesus
birth
biblical metaphor
biblical commandment
betrayal in love
bethlehem
benevolence
belief in resurrection
beer
beauty's decay
bass-soprano dialogue
baptismal promise
babylon's rivers
awakening of faith
awakening from sin
authority critique
augustus' wisdom
augustus' virtue
augustus' throne
augustus' son
artistry
artistic appreciation
art superiority
art of dying
arrival of time
arrival of messiah
archangel michael
appreciation of art and knowledge
apocalyptic destruction
anxiety
anticipation of the new year
anticipation of paradise
anticipation of joy
anticipation of heavenly peace
anticipation of heavenly joy
anticipation of afterlife
antichrist
anhalt's world
angelic worship
angelic wisdom
angelic service
angelic love
angelic choir
angelic assistance in death
ancient kingship
amidst enemies
amen
ambition
aid to the poor
agricultural metaphor
age and youth
age
affection
adornment
admiration for a teacher
admiration
adaptation to jesus
action
acknowledgment of sin
acknowledgement of sin
achievement
accountability
accompanying christ
acceptance of punishment
acceptance of god's will
acceptance of god's children
acceptance of fate
abundant love
absence of sorrow
absence of help
abiding in jesus
abandonment of conflict
abandonment
"""

system = """
You have a PhD in Lutheran theology from Harvard and are a genius at categorizing cantatas. The user has a lot of cantata categories that each correspond with just one cantata.
"""

response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": "Consider all the categories given. Group any very similar categories together. Make an exhausive, optimal grouping with no duplicates, and name each grouping.\n\n" + sample_lines(user)},
    ],
    temperature=0.8
)

# pprint(response)
print(response['choices'][0]['message']['content'])



