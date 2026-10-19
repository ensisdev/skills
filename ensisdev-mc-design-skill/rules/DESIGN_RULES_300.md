# DESIGN RULES — 300 NORMATIVE RULES

These rules are normative. An AI agent should treat them as defaults and document any deliberate exception.

## Typography & casing
001. Use small caps only for short labels, not paragraphs.
002. Keep player names in normal casing unless the product identity explicitly requires another treatment.
003. Use one primary heading treatment per screen family.
004. Do not fake small caps with random Unicode characters when real font support is unavailable.
005. Use bold/weight to establish hierarchy before adding decorative glyphs.
006. Do not use full uppercase for every GUI title.
007. Keep dynamic numeric values visually distinct from descriptive text.
008. Use sentence case for instructions when readability matters more than branding.
009. Use compact uppercase or small caps for metadata only when the line is short.
010. Keep action verbs visually prominent in interactive labels.

## Iconography & glyphs
011. Each icon must communicate object, action, state, or category.
012. Avoid using the same sparkle glyph on more than one semantic role.
013. Do not surround every title with decorative symbols.
014. Prefer meaningful Minecraft item icons when they improve recognition.
015. Set a decorative glyph budget for each surface.
016. Use one directional symbol consistently within a navigation family.
017. Do not use arrows as decoration when no action or direction exists.
018. Avoid mixing unrelated icon families on one screen.
019. Use icon repetition to show status only when the meaning is stable.
020. Remove an icon that adds no semantic information.

## GUI composition
021. Do not default every feature to a 9x6 chest.
022. Choose slot geometry from task priority, not habit.
023. Give the primary action a predictable location within a screen family.
024. Reserve navigation space only when navigation is actually needed.
025. Avoid decorative filler slots when content is already dense.
026. Use grouping to separate categories before adding borders.
027. Do not use glass panes as a universal frame.
028. Keep detail views visually distinct from collection views.
029. Use pagination only when content cannot be made scannable another way.
030. Do not put every button on the bottom row by default.

## Information architecture
031. Place the most decision-relevant information first.
032. Group data by user task, not by implementation class.
033. Separate discovery from action when the choice is complex.
034. Use progressive disclosure for advanced controls.
035. Avoid showing every available action at equal emphasis.
036. Make status and consequences obvious before destructive actions.
037. Keep comparison views aligned across comparable items.
038. Use consistent labels for the same concept across the plugin.
039. Do not duplicate the same state in multiple visual treatments unless needed.
040. Use empty states to explain what the player can do next.

## Messages
041. Every chat message starts with the plugin's gradient `[PluginName]` prefix; no separator glyph after it.
042. Put the result first for simple transactional messages.
043. Put the next action first when recovery is needed.
044. Use compact messages for repeated low-risk feedback.
045. Use structured messages for warnings that require a decision.
046. Avoid unnecessary punctuation as a substitute for hierarchy.
047. Do not make success/error distinguishable only by color.
048. Keep chat messages readable without hover effects.
049. Use context-first messages when players may not remember the triggering action.
050. Do not repeat the full command syntax when a concise action label is enough.

## Item names & lore
051. Make an item name identify the object before adding personality.
052. Do not use the same three-line lore structure for every item.
053. Keep mechanics separate from flavor when both are present.
054. Use section labels only when they improve scanning.
055. Keep action instructions explicit.
056. Put requirements near the action they gate.
057. Use aligned comparisons for upgrade or marketplace screens.
058. Avoid lore that repeats information already shown by the item name.
059. Keep dynamic values visually stable across similar items.
060. Do not hide important restrictions in flavor text.

## Color semantics
061. Assign colors semantic roles instead of choosing them line by line.
062. Do not use green for unrelated decorative accents everywhere.
063. Keep warning and destructive semantics consistent across surfaces.
064. Use neutral text for neutral information.
065. Avoid encoding a required distinction only by color.
066. Do not create a rainbow hierarchy with no semantic purpose.
067. Reserve accent color for interactive or brand-critical elements.
068. Use muted tones to reduce visual competition between secondary metadata.
069. Keep disabled states distinguishable without erasing legibility.
070. Do not change a status color arbitrarily between GUI and chat.

## Spacing & density
071. Use spacing to create groups before adding decorative borders.
072. Avoid filling every blank slot or line.
073. Use consistent rhythm within a component family.
074. Let high-priority information breathe.
075. Increase separation before adding another glyph.
076. Keep repeated list rows aligned.
077. Avoid dense walls of lore text when a concise label can replace them.
078. Use compact layouts only for genuinely high-frequency workflows.
079. Do not compress all controls merely to fit one more option.
080. Preserve a visual pause before destructive actions.

## Interaction & states
081. Design default, hover, click, disabled, empty, loading, success, and error states when applicable.
082. Do not make an action discoverable only through a decorative icon.
083. Keep confirmation actions clearly distinct from cancel actions.
084. Show current selection without relying on a single tiny marker.
085. Use progress feedback for actions that may take noticeable time.
086. Do not promise an action in lore that the click handler cannot perform.
087. Ensure unavailable actions explain why they are unavailable when useful.
088. Keep back/navigation behavior predictable within a feature family.
089. Avoid accidental destructive clicks by separating them from default actions.
090. Use hover details to augment, not replace, essential information.

## Localization & content
091. Design for longer translated strings.
092. Do not depend on English word length for alignment.
093. Keep placeholders semantically named.
094. Avoid embedding language-specific punctuation into reusable layout logic.
095. Do not build a visual hierarchy that collapses when a name becomes long.
096. Keep numeric formats locale-aware where the platform supports it.
097. Use consistent terminology for the same gameplay concept.
098. Do not abbreviate uncommon terms purely to save space.
099. Make pluralization and count wording adaptable.
100. Do not expose raw placeholder keys to players.

## Anti-patterns & review
101. Reject a redesign that changes only colors.
102. Reject a redesign that changes only glyphs.
103. Reject a redesign that changes only the title.
104. Compare new surfaces to at least three neighboring screens.
105. Record intentional exceptions to the rule set.
106. Prefer semantic variation over arbitrary visual novelty.
107. Do not add visual noise just to appear different.
108. Use a plugin-level design system record to preserve coherence.
109. Run a final copy/readability pass separately from a style pass.
110. Review unusual Unicode before shipping it.

## Typography & casing
111. Use small caps only for short labels, not paragraphs for a marketplace listing.
112. Use small caps only for short labels, not paragraphs for a profile menu.
113. Use small caps only for short labels, not paragraphs for a settings screen.
114. Use small caps only for short labels, not paragraphs for a quest tracker.
115. Use small caps only for short labels, not paragraphs for a reward screen.
116. Use small caps only for short labels, not paragraphs for a mailbox.
117. Use small caps only for short labels, not paragraphs for a confirmation dialog.
118. Use small caps only for short labels, not paragraphs for a paginated collection.
119. Use small caps only for short labels, not paragraphs for an admin utility.
120. Use small caps only for short labels, not paragraphs for a chat notification.
121. Use small caps only for short labels, not paragraphs for an item lore block.
122. Use small caps only for short labels, not paragraphs for a scoreboard panel.
123. Use small caps only for short labels, not paragraphs for a tablist section.
124. Use small caps only for short labels, not paragraphs for a bossbar message.
125. Use small caps only for short labels, not paragraphs for a hologram.
126. Use small caps only for short labels, not paragraphs for an onboarding flow.
127. Use small caps only for short labels, not paragraphs for an upgrade interface.
128. Use small caps only for short labels, not paragraphs for a party/guild screen.
129. Use small caps only for short labels, not paragraphs for a teleport menu.
130. Use small caps only for short labels, not paragraphs for a help/command screen.
131. Use small caps only for short labels, not paragraphs for a high-frequency action.
132. Use small caps only for short labels, not paragraphs for a low-frequency advanced tool.
133. Use small caps only for short labels, not paragraphs for an empty state.
134. Use small caps only for short labels, not paragraphs for an error state.
135. Use small caps only for short labels, not paragraphs for a success state.
136. Keep player names in normal casing unless the product identity explicitly requires another treatment for a marketplace listing.
137. Keep player names in normal casing unless the product identity explicitly requires another treatment for a profile menu.
138. Keep player names in normal casing unless the product identity explicitly requires another treatment for a settings screen.
139. Keep player names in normal casing unless the product identity explicitly requires another treatment for a quest tracker.
140. Keep player names in normal casing unless the product identity explicitly requires another treatment for a reward screen.
141. Keep player names in normal casing unless the product identity explicitly requires another treatment for a mailbox.
142. Keep player names in normal casing unless the product identity explicitly requires another treatment for a confirmation dialog.
143. Keep player names in normal casing unless the product identity explicitly requires another treatment for a paginated collection.
144. Keep player names in normal casing unless the product identity explicitly requires another treatment for an admin utility.
145. Keep player names in normal casing unless the product identity explicitly requires another treatment for a chat notification.
146. Keep player names in normal casing unless the product identity explicitly requires another treatment for an item lore block.
147. Keep player names in normal casing unless the product identity explicitly requires another treatment for a scoreboard panel.
148. Keep player names in normal casing unless the product identity explicitly requires another treatment for a tablist section.
149. Keep player names in normal casing unless the product identity explicitly requires another treatment for a bossbar message.
150. Keep player names in normal casing unless the product identity explicitly requires another treatment for a hologram.
151. Keep player names in normal casing unless the product identity explicitly requires another treatment for an onboarding flow.
152. Keep player names in normal casing unless the product identity explicitly requires another treatment for an upgrade interface.
153. Keep player names in normal casing unless the product identity explicitly requires another treatment for a party/guild screen.
154. Keep player names in normal casing unless the product identity explicitly requires another treatment for a teleport menu.
155. Keep player names in normal casing unless the product identity explicitly requires another treatment for a help/command screen.
156. Keep player names in normal casing unless the product identity explicitly requires another treatment for a high-frequency action.
157. Keep player names in normal casing unless the product identity explicitly requires another treatment for a low-frequency advanced tool.
158. Keep player names in normal casing unless the product identity explicitly requires another treatment for an empty state.
159. Keep player names in normal casing unless the product identity explicitly requires another treatment for an error state.
160. Keep player names in normal casing unless the product identity explicitly requires another treatment for a success state.
161. Use one primary heading treatment per screen family for a marketplace listing.
162. Use one primary heading treatment per screen family for a profile menu.
163. Use one primary heading treatment per screen family for a settings screen.
164. Use one primary heading treatment per screen family for a quest tracker.
165. Use one primary heading treatment per screen family for a reward screen.
166. Use one primary heading treatment per screen family for a mailbox.
167. Use one primary heading treatment per screen family for a confirmation dialog.
168. Use one primary heading treatment per screen family for a paginated collection.
169. Use one primary heading treatment per screen family for an admin utility.
170. Use one primary heading treatment per screen family for a chat notification.
171. Use one primary heading treatment per screen family for an item lore block.
172. Use one primary heading treatment per screen family for a scoreboard panel.
173. Use one primary heading treatment per screen family for a tablist section.
174. Use one primary heading treatment per screen family for a bossbar message.
175. Use one primary heading treatment per screen family for a hologram.
176. Use one primary heading treatment per screen family for an onboarding flow.
177. Use one primary heading treatment per screen family for an upgrade interface.
178. Use one primary heading treatment per screen family for a party/guild screen.
179. Use one primary heading treatment per screen family for a teleport menu.
180. Use one primary heading treatment per screen family for a help/command screen.
181. Use one primary heading treatment per screen family for a high-frequency action.
182. Use one primary heading treatment per screen family for a low-frequency advanced tool.
183. Use one primary heading treatment per screen family for an empty state.
184. Use one primary heading treatment per screen family for an error state.
185. Use one primary heading treatment per screen family for a success state.
186. Do not fake small caps with random Unicode characters when real font support is unavailable for a marketplace listing.
187. Do not fake small caps with random Unicode characters when real font support is unavailable for a profile menu.
188. Do not fake small caps with random Unicode characters when real font support is unavailable for a settings screen.
189. Do not fake small caps with random Unicode characters when real font support is unavailable for a quest tracker.
190. Do not fake small caps with random Unicode characters when real font support is unavailable for a reward screen.
191. Do not fake small caps with random Unicode characters when real font support is unavailable for a mailbox.
192. Do not fake small caps with random Unicode characters when real font support is unavailable for a confirmation dialog.
193. Do not fake small caps with random Unicode characters when real font support is unavailable for a paginated collection.
194. Do not fake small caps with random Unicode characters when real font support is unavailable for an admin utility.
195. Do not fake small caps with random Unicode characters when real font support is unavailable for a chat notification.
196. Do not fake small caps with random Unicode characters when real font support is unavailable for an item lore block.
197. Do not fake small caps with random Unicode characters when real font support is unavailable for a scoreboard panel.
198. Do not fake small caps with random Unicode characters when real font support is unavailable for a tablist section.
199. Do not fake small caps with random Unicode characters when real font support is unavailable for a bossbar message.
200. Do not fake small caps with random Unicode characters when real font support is unavailable for a hologram.
201. Do not fake small caps with random Unicode characters when real font support is unavailable for an onboarding flow.
202. Do not fake small caps with random Unicode characters when real font support is unavailable for an upgrade interface.
203. Do not fake small caps with random Unicode characters when real font support is unavailable for a party/guild screen.
204. Do not fake small caps with random Unicode characters when real font support is unavailable for a teleport menu.
205. Do not fake small caps with random Unicode characters when real font support is unavailable for a help/command screen.
206. Do not fake small caps with random Unicode characters when real font support is unavailable for a high-frequency action.
207. Do not fake small caps with random Unicode characters when real font support is unavailable for a low-frequency advanced tool.
208. Do not fake small caps with random Unicode characters when real font support is unavailable for an empty state.
209. Do not fake small caps with random Unicode characters when real font support is unavailable for an error state.
210. Do not fake small caps with random Unicode characters when real font support is unavailable for a success state.
211. Use bold/weight to establish hierarchy before adding decorative glyphs for a marketplace listing.
212. Use bold/weight to establish hierarchy before adding decorative glyphs for a profile menu.
213. Use bold/weight to establish hierarchy before adding decorative glyphs for a settings screen.
214. Use bold/weight to establish hierarchy before adding decorative glyphs for a quest tracker.
215. Use bold/weight to establish hierarchy before adding decorative glyphs for a reward screen.
216. Use bold/weight to establish hierarchy before adding decorative glyphs for a mailbox.
217. Use bold/weight to establish hierarchy before adding decorative glyphs for a confirmation dialog.
218. Use bold/weight to establish hierarchy before adding decorative glyphs for a paginated collection.
219. Use bold/weight to establish hierarchy before adding decorative glyphs for an admin utility.
220. Use bold/weight to establish hierarchy before adding decorative glyphs for a chat notification.
221. Use bold/weight to establish hierarchy before adding decorative glyphs for an item lore block.
222. Use bold/weight to establish hierarchy before adding decorative glyphs for a scoreboard panel.
223. Use bold/weight to establish hierarchy before adding decorative glyphs for a tablist section.
224. Use bold/weight to establish hierarchy before adding decorative glyphs for a bossbar message.
225. Use bold/weight to establish hierarchy before adding decorative glyphs for a hologram.
226. Use bold/weight to establish hierarchy before adding decorative glyphs for an onboarding flow.
227. Use bold/weight to establish hierarchy before adding decorative glyphs for an upgrade interface.
228. Use bold/weight to establish hierarchy before adding decorative glyphs for a party/guild screen.
229. Use bold/weight to establish hierarchy before adding decorative glyphs for a teleport menu.
230. Use bold/weight to establish hierarchy before adding decorative glyphs for a help/command screen.
231. Use bold/weight to establish hierarchy before adding decorative glyphs for a high-frequency action.
232. Use bold/weight to establish hierarchy before adding decorative glyphs for a low-frequency advanced tool.
233. Use bold/weight to establish hierarchy before adding decorative glyphs for an empty state.
234. Use bold/weight to establish hierarchy before adding decorative glyphs for an error state.
235. Use bold/weight to establish hierarchy before adding decorative glyphs for a success state.
236. Do not use full uppercase for every GUI title for a marketplace listing.
237. Do not use full uppercase for every GUI title for a profile menu.
238. Do not use full uppercase for every GUI title for a settings screen.
239. Do not use full uppercase for every GUI title for a quest tracker.
240. Do not use full uppercase for every GUI title for a reward screen.
241. Do not use full uppercase for every GUI title for a mailbox.
242. Do not use full uppercase for every GUI title for a confirmation dialog.
243. Do not use full uppercase for every GUI title for a paginated collection.
244. Do not use full uppercase for every GUI title for an admin utility.
245. Do not use full uppercase for every GUI title for a chat notification.
246. Do not use full uppercase for every GUI title for an item lore block.
247. Do not use full uppercase for every GUI title for a scoreboard panel.
248. Do not use full uppercase for every GUI title for a tablist section.
249. Do not use full uppercase for every GUI title for a bossbar message.
250. Do not use full uppercase for every GUI title for a hologram.
251. Do not use full uppercase for every GUI title for an onboarding flow.
252. Do not use full uppercase for every GUI title for an upgrade interface.
253. Do not use full uppercase for every GUI title for a party/guild screen.
254. Do not use full uppercase for every GUI title for a teleport menu.
255. Do not use full uppercase for every GUI title for a help/command screen.
256. Do not use full uppercase for every GUI title for a high-frequency action.
257. Do not use full uppercase for every GUI title for a low-frequency advanced tool.
258. Do not use full uppercase for every GUI title for an empty state.
259. Do not use full uppercase for every GUI title for an error state.
260. Do not use full uppercase for every GUI title for a success state.
261. Keep dynamic numeric values visually distinct from descriptive text for a marketplace listing.
262. Keep dynamic numeric values visually distinct from descriptive text for a profile menu.
263. Keep dynamic numeric values visually distinct from descriptive text for a settings screen.
264. Keep dynamic numeric values visually distinct from descriptive text for a quest tracker.
265. Keep dynamic numeric values visually distinct from descriptive text for a reward screen.
266. Keep dynamic numeric values visually distinct from descriptive text for a mailbox.
267. Keep dynamic numeric values visually distinct from descriptive text for a confirmation dialog.
268. Keep dynamic numeric values visually distinct from descriptive text for a paginated collection.
269. Keep dynamic numeric values visually distinct from descriptive text for an admin utility.
270. Keep dynamic numeric values visually distinct from descriptive text for a chat notification.
271. Keep dynamic numeric values visually distinct from descriptive text for an item lore block.
272. Keep dynamic numeric values visually distinct from descriptive text for a scoreboard panel.
273. Keep dynamic numeric values visually distinct from descriptive text for a tablist section.
274. Keep dynamic numeric values visually distinct from descriptive text for a bossbar message.
275. Keep dynamic numeric values visually distinct from descriptive text for a hologram.
276. Keep dynamic numeric values visually distinct from descriptive text for an onboarding flow.
277. Keep dynamic numeric values visually distinct from descriptive text for an upgrade interface.
278. Keep dynamic numeric values visually distinct from descriptive text for a party/guild screen.
279. Keep dynamic numeric values visually distinct from descriptive text for a teleport menu.
280. Keep dynamic numeric values visually distinct from descriptive text for a help/command screen.
281. Keep dynamic numeric values visually distinct from descriptive text for a high-frequency action.
282. Keep dynamic numeric values visually distinct from descriptive text for a low-frequency advanced tool.
283. Keep dynamic numeric values visually distinct from descriptive text for an empty state.
284. Keep dynamic numeric values visually distinct from descriptive text for an error state.
285. Keep dynamic numeric values visually distinct from descriptive text for a success state.
286. Use sentence case for instructions when readability matters more than branding for a marketplace listing.
287. Use sentence case for instructions when readability matters more than branding for a profile menu.
288. Use sentence case for instructions when readability matters more than branding for a settings screen.
289. Use sentence case for instructions when readability matters more than branding for a quest tracker.
290. Use sentence case for instructions when readability matters more than branding for a reward screen.
291. Use sentence case for instructions when readability matters more than branding for a mailbox.
292. Use sentence case for instructions when readability matters more than branding for a confirmation dialog.
293. Use sentence case for instructions when readability matters more than branding for a paginated collection.
294. Use sentence case for instructions when readability matters more than branding for an admin utility.
295. Use sentence case for instructions when readability matters more than branding for a chat notification.
296. Use sentence case for instructions when readability matters more than branding for an item lore block.
297. Use sentence case for instructions when readability matters more than branding for a scoreboard panel.
298. Use sentence case for instructions when readability matters more than branding for a tablist section.
299. Use sentence case for instructions when readability matters more than branding for a bossbar message.
300. Use sentence case for instructions when readability matters more than branding for a hologram.
