import { ComponentModelBase } from "@/components/base-classes/component-model-base";
import type { PageModel } from "@/data/models/page-model";
import { BuilderUtilities } from "@/utilities/builder-utilities";

/**
 *  Model for the page editor component.
 */
class PageEditorModel extends ComponentModelBase {
    /**
	 * Specifies the localization namespace to use for getting localized text values.
	 */
	protected getLocalizationNamespace(): string {
		return "page-editor";
	}

	public getSrcDoc() : string {
		return `
			<html>
				<head>
				    <link rel="stylesheet" href="/css/paper.min.css">
				    <link rel="stylesheet" href="/css/page-editor.css">
				</head>
				<body></body>
			</html>
		`;
	}

	public onPageLoad(pages: Array<PageModel>, activePage: PageModel, addWidgetToPage: Function): void {
		const pageEditor: HTMLIFrameElement = document.getElementById(`${activePage.properties.id}-editor`) as HTMLIFrameElement;
		const pageElement: HTMLElement = BuilderUtilities.getPageElementById(activePage.properties.id);
		pageElement.style.display = "grid";
		pageEditor.contentDocument?.body.insertBefore(pageElement, pageEditor.contentDocument?.body.firstChild);
	}
}

export const component = new PageEditorModel();
